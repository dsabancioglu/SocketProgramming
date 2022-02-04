#pylint: skip-file
from queue import Empty
from tkinter import *
import tkinter as tk
import socket

from ..widgets.server_widgets import ServerWidgets


class Server: 
    
    def __init__(self):
        self.ip_var = tk.StringVar()
        self.port_var = tk.StringVar()
        self.socket = socket.socket()
        self.socket.setblocking(0)
        self.max_connection = 5
        self.active = 0
        self.listen_mode = 0
        self.serverWidgets = ServerWidgets(self)
        
    # def create_widgets(self, server, client):
    #     self.serverWidgets = ServerWidgets(server, client) #bunu init e tasi
    #     self.created = 1 #bunu widget a tasi

    def bind(self,event):
        ip = self.ip_var.get()
        port = int(self.port_var.get())
        print(port, ip)
        try:
            self.socket.bind((ip, port))
            print("Socket binded to %s port\n" %(port))
            self.active = 1
            self.serverWidgets.server_status_value.config(text="Run",foreground="#278c3d")
            self.listen_port()

        except:
            print ('\n\nBind failed') 
            self.active = 0
            self.status = "passive"
            self.serverWidgets.server_status_value.config(text="Stop", foreground="#eb3838")

    def listen_port(self):
        self.socket.listen(self.max_connection) #listens port untill got client connect request
        self.accept_connection() #after client request came, server accept connection request (3-way handshake completed)
        
        """while True: 
            if(self.listen_mode):
                self.get_message()"""

    def accept_connection(self): #waiting request from the client
        print("before accept")
        self.c,self.addr = self.socket.accept() #prog burada takili kaliyor
        print("before accept")
        print ('\nGot connection from', self.addr) 
        self.listen_mode = 1

    def send_message_to_client(self,event):
        message = self.serverWidgets.send_client_entry.get('1.0','end')
        self.c.send(message.encode())
    
    def get_message(self):
        while True:
            if(self.listen_mode and self.c.recv(1024) != ""):
                self.receivedMessage = self.c.recv(1024)
                print(self.receivedMessage)
                self.serverWidgets.received_client_entry.insert("end", self.receivedMessage)

    def close_connection(self,event): #bunun da butonunu ekle
        self.c.close()
        self.listen_mode = 0
        self.active = 0
        #stop thread
        self.serverWidgets.server_status_value.config(text="Stop", foreground="#eb3838")
        print("Connection closed")
    
    def delete_entry(self,event):
        self.serverWidgets.received_client_entry.delete('1.0', END)
        