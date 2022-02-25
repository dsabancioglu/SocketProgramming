#pylint: skip-file
import threading
import tkinter as tk
import socket

from ..widgets.server_widgets import ServerWidgets

class Server: 
    
    def __init__(self):
        print(  "server create function")
        self.ip_var = tk.StringVar()
        self.port_var = tk.StringVar()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.socket.setblocking(0)
        self.max_connection = 5
        self.serverWidgets = ServerWidgets(self)
        
    def bind(self,event):
        ip = self.ip_var.get()
        port = int(self.port_var.get())
        print(port, ip)
        try:
            self.socket.bind((ip, port))
            print("Socket binded to %s port\n" %(port))
            self.serverWidgets.server_status_value.config(text="Run",foreground="#278c3d") #hata veriyor 
            self.socket.listen(self.max_connection)
            self.listen = True
        except:
            print ('\n\nBind failed') 
            self.serverWidgets.server_status_value.config(text="Stop", foreground="#eb3838")

        if(self.listen):
            print('Waiting for a Connection..')
            self.client_count = 0
            #self.accept_connection()

            

    def accept_connection(self): #waiting request from the client
        # while True:

        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect(('localhost', 6789))
        self.clientSocket.sendall(('Hello, world').encode())

        self.connection, self.address = self.socket.accept() #programın burda durmasi client i etkilemesin, o yüzden client ve server'ı ayrı 2 thread ya da process olarak çlıştır
        print('Connected to: ' + self.address[0] + ':'.format(self.address[1]))
        get_message_thread = threading.Thread(target=self.get_message, args=(self.connection,)) #her client connection ını ayrı ayrı threadlerde dinlicez
        get_message_thread.start()
        self.client_count += 1
        print('Thread Number: '.format(self.client_count))

    def send_message_to_client(self,event):
        message = self.serverWidgets.send_client_entry.get('1.0','end')
        self.connection.send(message.encode())
    
    def get_message(self,connection):   #ayri bir thread olarak calistigi icin programin diger bolumlerinden bagimsiz gibi dusunebilirsin.
        connection.send(str.encode('Welcome to the Servern'))
        while True:
                self.receivedMessage = self.connection.recv(1024)
                if not self.receivedMessage:
                    continue
                else:
                    print(self.receivedMessage)
                    self.serverWidgets.received_client_entry.insert("end", self.receivedMessage)

    def close_connection(self,event): #bunun da butonunu ekle
        self.connection.close()
        self.listen_mode = 0
        self.active = 0
        #stop thread
        self.serverWidgets.server_status_value.config(text="Stop", foreground="#eb3838")
        print("Connection closed")
    
    def delete_entry(self,event):
        self.serverWidgets.received_client_entry.delete('1.0', 'end')
        