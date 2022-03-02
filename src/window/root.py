#pylint: skip-file
from tkinter import *
import tkinter as tk

from ..socket.client import Client
from ..socket.server import Server

class Root:
    def __init__(self):
        self.root = Tk()
        self.root.title("Client Server Communication")
        self.root.geometry('200x150+80+80')
        self.server_button = tk.Button(self.root, text="Server", command=self.create_server).grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
        self.client_button = tk.Button(self.root, text="Client", command=self.create_client).grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
        self.root.mainloop()
    
    def create_server(self):
        print("\nserver")
        self.server = Server()

    def create_client(self):   
        print(  "\nclient")
        self.client = Client()





