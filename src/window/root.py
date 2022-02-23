#pylint: skip-file
from ast import arg
from tkinter import *
import tkinter as tk
import multiprocessing

# from ..widgets.client_widgets import ClientWidgets
# from ..widgets.server_widgets import ServerWidgets
from ..socket.client import Client
from ..socket.server import Server

class Root:
    def __init__(self):
        self.root = Tk()
        self.root.title("Client Server Communication")
        self.root.geometry('900x500+500+250')
        self.server_button = tk.Button(self.root, text="Server", command=self.create_server).grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
        self.client_button = tk.Button(self.root, text="Client", command=self.create_client).grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
        self.root.mainloop()
    
    #her window ayri 1 process olarak calisacak
    def create_server(self):
        print(  "server")
        # self.server = Server()  #thread olarak calistir
        server = Server()
        self.server_process = multiprocessing.Process(target=server.__init__, args=(server,)) #Bunu düzelt
        print(  "server")
        self.server_process.start()
        print(  "server")
        # self.server_thread = ServerWidgets() #create server thread
        # self.server_thread.start() #start server thread
    
    def create_client(self):   #thread olarak calistir
        print(  "client")
        client = Client()
        self.client_process = multiprocessing.Process(target=client.__init__, args=(client,))
        self.client_process.start()
        # self.client_thread = ClientWidgets()  #create client thread
        # self.server_thread.start()  #start client thread

''' NOT: Her Window ayrı 1 process olarak çalışacak (Server Window/Client Window), Her process içinde de sürekli çalışan(sürekli mesaj dinleyen) bir thread var ---> get_message()'''



