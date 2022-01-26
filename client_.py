#pylint: skip-file
from tkinter import *
#from client_server import connection_statement_value, send_server_entry, received_server_entry,server
from server_ import Server
import socket


class Client:
    def __init__(self):
        self.ip_var = StringVar()
        self.port_var = StringVar()
        self.socket = socket.socket()

    def get_connection(self,event,connection_statement_value, server):
        ip = self.ip_var.get()
        port= int(self.port_var.get())
        
        try:
            self.socket.connect((ip, port))
            print("\nconnection established")
            connection_statement_value.config(text="Connected", foreground="#278c3d")
            server.accept_connection()
        except:
            print("\nConnection could not be established" )
            connection_statement_value.config(text="Not connected", foreground="eb3838")

    def send_message_to_server(self,event,send_server_entry):
        message = send_server_entry.get('1.0','end').encode()
        print(message)
        self.socket.send(message)

    def get_message(self,event,received_server_entry):
        self.receivedMessage = self.socket.recv(1024)
        received_server_entry.insert(1.0,self.receivedMessage)

    def close_connection(self):
        self.socket.close()
        print("closed")
        
    def delete_entry(self,event,received_server_entry):
        received_server_entry.delete('1.0', END)

