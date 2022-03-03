#pylint: skip-file
import threading
from tkinter import *
import socket
import logging
import datetime
import sys

sys.dont_write_bytecode = True

from ..widgets.client_widgets import ClientWidgets
from ..logger.logger import setup_logger


class Client:

    def __init__(self):
        self.ip_var = StringVar()
        self.port_var = StringVar()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger = setup_logger("client_")
        self.clientWidgets = ClientWidgets(self)


    def get_connection(self,event):
        ip = self.ip_var.get()
        port= int(self.port_var.get())
        
        try:
            self.socket.connect((ip, port))
            print("Client: connection established")
            self.clientWidgets.connection_statement_value.config(text="Connected", foreground="#278c3d")
            get_message_thread = threading.Thread(target=self.get_message) #her client connection ını ayrı ayrı threadlerde dinlicez
            get_message_thread.start()
        except socket.error as msg:
            print("Client:Connection could not be established, error message : {}".format(msg) )
            self.clientWidgets.connection_statement_value.config(text="Not connected", foreground="#eb3838")

    def send_message_to_server(self,event):
        message = self.clientWidgets.send_server_entry.get('1.0','end').encode()
        self.logger.info("Sended message:   {}". format(message))
        print("Client: sended message -> {}". format(message))
        self.socket.send(message)

    def get_message(self):
        while True:
            self.receivedMessage = self.socket.recv(1024)
            self.logger.info("Received message: {}". format(self.receivedMessage))
            if not self.receivedMessage: #empty string gelirse dur
                continue
            else:
                self.clientWidgets.received_server_entry.insert(1.0,self.receivedMessage)

    def close_connection(self, event): #buton oluştur buna, event alcak
        self.socket.close()
        self.listen_mode = 0
        self.active = 0
        self.clientWidgets.connection_statement_value.config(text="Not connected", foreground="#eb3838")
        print("closed")
        #thread i sonlandır
        
    def delete_entry(self,event):
        self.clientWidgets.received_server_entry.delete('1.0', END)

    def setup_logger(self):
        now = datetime.datetime.now().strftime("%x").replace("/",".") 
        file_name = "client_" + now + ".log"
        logger = logging.getLogger("client logger")
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(file_name)
        formatter = logging.Formatter('%(asctime)s %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger