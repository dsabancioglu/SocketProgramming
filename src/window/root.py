#pylint: skip-file
from tkinter import *
import tkinter as tk
import multiprocessing

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
        self.server = Server()
        # print(  "server before thread")
        # self.server_process = multiprocessing.Process(target=self.server.serverWidgets.create) #Bunu düzelt
        # print(  "server process created")
        # self.server_process.start()
        # print(  "server process started")
        # self.server_thread = ServerWidgets() #create server thread
        # self.server_thread.start() #start server thread
    
    def create_client(self):   
        print(  "client")
        self.client = Client() #boyle yapinca window yaratiliyor ama bu satirdan sonrasi calismiyor, yani process olusmuyor
        # self.client_process = multiprocessing.Process(target=client.__init__)
        # print(  "client process created")
        # self.client_process.start()
        # print(  "client process started")
        # self.client_thread = ClientWidgets()  #create client thread
        # self.server_thread.start()  #start client thread

''' NOT: Her Window ayrı 1 process olarak çalışacak (Server Window/Client Window), Her process içinde de sürekli çalışan(sürekli mesaj dinleyen) bir thread var ---> get_message()'''



