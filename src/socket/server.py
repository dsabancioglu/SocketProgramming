#pylint: skip-file
import threading
import tkinter as tk
import socket
import logging
import datetime

 # logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%I:%M:%S')

from ..widgets.server_widgets import ServerWidgets

class Server:     
    def __init__(self):
        print(  "server create function")
        self.ip_var = tk.StringVar()
        self.port_var = tk.StringVar()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.max_connection = 5
        self.listen = False
        self.logger = self.setup_logger()
        self.serverWidgets = ServerWidgets(self)

    def setup_logger(self):
        now = datetime.datetime.now().strftime("%x").replace("/",".") 
        file_name = "server_" + now + ".log"
        logger = logging.getLogger("server logger")
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(file_name)
        formatter = logging.Formatter('%(asctime)s %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def bind(self,event):
        ip = self.ip_var.get()
        port = int(self.port_var.get())
        print("Server: {} , {}" .format(port, ip))
        try:
            self.socket.bind((ip, port))
            print("Server: Socket binded to %s port\n" %(port))
            self.serverWidgets.server_status_value.config(text="Run",foreground="#278c3d") 
            self.socket.listen(self.max_connection)
            self.listen = True
        except socket.error as message:
            print ('Server: Bind failed, error : {}'.format(message)) 
            self.serverWidgets.server_status_value.config(text="Stop", foreground="#eb3838")

        if(self.listen):
            print('Server: Waiting for a Connection..')
            self.client_count = 0
            accept_connection_thread = threading.Thread(target=self.accept_connection) #accept connection'i thread olarak calistirdigimiz icin program accept() metodunda bloklanmaz.
            accept_connection_thread.start()            

    def accept_connection(self): 
        
        while True:
            self.connection, self.address = self.socket.accept() 
            print('Server: Connected to: ' + self.address[0] + ': {}'.format(self.address[1]))
            print(self.client_count)
            self.client_count += 1
            print(self.client_count)
            print('Server: Thread Number: {}'.format(self.client_count))
            get_message_thread = threading.Thread(target=self.get_message, args=(self.connection,)) #her client connection ını ayrı ayrı threadlerde dinlicez
            get_message_thread.start()

    def send_message_to_client(self,event):
        self.message = self.serverWidgets.send_client_entry.get('1.0','end')
        self.logger.info("Sended message:   {}". format(self.message))
        self.connection.send(self.message.encode())
    
    def get_message(self,connection):   #her connection icin surekli olarak dinleme yapar
        print("Server: get_message thread created")
        connection.send(str.encode('Welcome to the Server'))
        while True:
                self.receivedMessage = self.connection.recv(1024)  #program mesaj gelene kadar burada bekler
                self.logger.info("Received message: {}". format(self.receivedMessage))
                if not self.receivedMessage:
                    continue
                else:
                    print("Server: received message (server): {}".format(self.receivedMessage))
                    self.serverWidgets.received_client_entry.insert("end", self.receivedMessage)  

    def close_connection(self,event): #bunun da butonunu ekle
        self.connection.close()
        self.listen_mode = 0
        self.active = 0
        #stop thread
        self.serverWidgets.server_status_value.config(text="Stop", foreground="#eb3838")
        print("Server: Connection closed")
    
    def delete_entry(self,event):
        self.serverWidgets.received_client_entry.delete('1.0', 'end')
        