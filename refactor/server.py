#pylint: skip-file
from tkinter import *
import tkinter as tk
from widgets import server_status_value, send_client_entry, received_client_entry
import socket

class Server:
    def __init__(self):
        self.ip_var = tk.StringVar()
        self.port_var = tk.StringVar()
        self.socket = socket.socket()
        self.max_connection = 5
        self.active = FALSE
    
    def bind(self,event):
        ip = self.ip_var.get()
        port = int(self.port_var.get())
        print(port)
        try:
            self.socket.bind((ip, port))
            print("Socket binded to %s port\n" %(port))
            self.active = 1
            server_status_value.config(text="Run",foreground="#278c3d")

        except:
            print ('\n\nBind failed') 
            self.active = 0
            self.status = "passive"
            server_status_value.config(text="Stop", foreground="eb3838")

        #listen port
        if(self.active):
            self.socket.listen(self.max_connection)
            print("socket is listening\n")

    def accept_connection(self): #waiting request from the client
        self.c,self.addr = self.socket.accept()
        print ('\nGot connection from', self.addr) 

    def send_message_to_client(self,event): #bu fonku mainde tanımla circular dependency yi azalt
        message = send_client_entry.get('1.0','end')
        self.c.send(message.encode())
    
    def get_message(self,event):
        self.receivedMessage = self.c.recv(1024)
        print(self.receivedMessage)
        received_client_entry.insert("end", self.receivedMessage)

    def close_connection(self):
        self.c.close()
        print("Connection closed")
    
    def delete_entry(self,event):
        received_client_entry.delete('1.0', END)
