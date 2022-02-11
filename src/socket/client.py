#pylint: skip-file
import threading
from tkinter import *
import socket

# from ..widgets.client_widgets import ClientWidgets


class Client:

    def __init__(self, clientWidgets):
        self.ip_var = StringVar()
        self.port_var = StringVar()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.clientWidgets = ClientWidgets(self)
        self.clientWidgets = clientWidgets

    def get_connection(self,event):
        ip = self.ip_var.get()
        port= int(self.port_var.get())
        
        try:
            self.socket.connect((ip, port))
            print("\nconnection established")
            self.clientWidgets.connection_statement_value.config(text="Connected", foreground="#278c3d")
            get_message_thread = threading.Thread(target=self.get_message) #her client connection ını ayrı ayrı threadlerde dinlicez
            get_message_thread.start()
        except:
            print("\nConnection could not be established" )
            self.clientWidgets.connection_statement_value.config(text="Not connected", foreground="#eb3838")

    def send_message_to_server(self,event):
        message = self.clientWidgets.send_server_entry.get('1.0','end').encode()
        print(message)
        self.socket.send(message)

    def get_message(self):
        while True:
            self.receivedMessage = self.socket.recv(1024)
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