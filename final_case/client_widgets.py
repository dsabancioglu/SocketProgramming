#pylint: skip-file
from tkinter import *
from tkinter import ttk
import tkinter as tk

from root import *


class ClientWidgets:

    def __init__(self, server, client):
        #Client Frame
        self.client_frame = ttk.Frame(root)
        self.client_frame.columnconfigure(0, weight=1)
        self.client_frame.columnconfigure(1, weight=1)
        self.client_frame.pack(fill=BOTH, side=RIGHT , expand=True)

        #Client widgets
        self.client_label = ttk.Label(self.client_frame, text="Client")
        self.client_label.grid(column=0, row=0, sticky=tk.E, padx=5 ,pady=5)

        self.client_ip = ttk.Label(self.client_frame, text="Ip:").grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
        self.client_ip_entry = ttk.Entry(self.client_frame, textvariable=client.ip_var).grid(column=1, row=1, sticky=tk.W, padx=20,pady=5)

        self.client_port = ttk.Label(self.client_frame, text="Port:").grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
        self.client_port_entry = ttk.Entry(self.client_frame,textvariable=client.port_var).grid(column=1, row=2, sticky=tk.W, padx=20, pady=5)

        self.connect_button = tk.Button(self.client_frame, text="Connect Server",background="#54727a",foreground="white")
        self.connect_button.grid(column=1, row=3, sticky=tk.NS, padx=20, pady=5) #is active i triggerlamasi lazim event bind edicez
        self.connect_button.bind("<Button-1>", client.get_connection)

        self.connection_statement = ttk.Label(self.client_frame, text="Connection Statement:").grid(column=0,row=4, sticky=tk.W, padx=20,pady=20)
        self.connection_statement_value = ttk.Label(self.client_frame, text="Not connected", foreground="red")
        self.connection_statement_value.grid(column=1,row=4, sticky=tk.EW, padx=20,pady=20)

        self.send_server = ttk.Label(self.client_frame, text="Send message to server:").grid(column=0,row=5, sticky=tk.W, padx=20,pady=0)
        self.send_server_entry = tk.Text(self.client_frame, width=20, height=3)
        self.send_server_entry.grid(column=0,row=6,sticky=tk.EW, padx=20,pady=5, columnspan=2)

        self.send_button_client = tk.Button(self.client_frame, text="SEND", background="#278c3d", foreground="white")
        self.send_button_client.grid(column=1, row=7, sticky=E, pady=5, padx=20)
        self.send_button_client.bind("<Button-1>", client.send_message_to_server)
        self.send_button_client.bind("<Button-1>", server.get_message, add='+')

        self.received_server = ttk.Label(self.client_frame, text="Received message from Server:").grid(column=0,row=8,sticky=tk.W, padx=20,pady=15)
        self.received_server_entry = tk.Text(self.client_frame, width=20,height=3) 
        self.received_server_entry.grid(column=0 ,row=9 ,sticky= EW,padx=20,pady=0, columnspan=2)

        self.delete_button_client = tk.Button(self.client_frame, text="DELETE", background="#eb3838", foreground="white")
        self.delete_button_client.grid(column=1, row=10, sticky=E, pady=5, padx=20)
        self.delete_button_client.bind("<Button-1>", client.delete_entry)

        