#pylint: skip-file
from tkinter import *
from tkinter import ttk
import tkinter as tk
import sys

sys.dont_write_bytecode = True


class ServerWidgets:
    def __init__(self,server):   
        print(  "serverWidgets init")
        self.server_frame = Toplevel()
        self.server_frame.geometry('500x500+50+300')
        self.server_frame.title("Server")
        self.server_frame.columnconfigure(0, weight=1)
        self.server_frame.columnconfigure(1, weight=1)

        self.server_ip = ttk.Label(self.server_frame, text="Ip:").grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
        self.server_ip_entry = ttk.Entry(self.server_frame, textvariable=server.ip_var).grid(column=1, row=1, sticky=tk.W, padx=20,pady=5)

        self.server_port = ttk.Label(self.server_frame, text="Port:").grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
        self.server_port_entry = ttk.Entry(self.server_frame, textvariable=server.port_var).grid(column=1, row=2, sticky=tk.W, padx=20, pady=5)

        self.listen_button = tk.Button(self.server_frame, text="Run Server",background="#54727a",foreground="white")
        self.listen_button.grid(column=1, row=3, sticky=tk.NS, padx=20, pady=5)
        self.listen_button.bind("<Button-1>", server.bind)

        self.stop_button = tk.Button(self.server_frame, text="Stop Server",background="#54727a",foreground="white")
        self.stop_button.grid(column=0, row=3, sticky=tk.E, padx=0, pady=5) 
        self.stop_button.bind("<Button-1>", server.close_connection)

        self.server_status = ttk.Label(self.server_frame, text="Server Status:").grid(column=0,row=4, sticky=tk.W, padx=20,pady=20)
        self.server_status_value = ttk.Label(self.server_frame, text="Stop", foreground="red")
        self.server_status_value.grid(column=1,row=4, sticky=tk.EW, padx=20,pady=20) 

        self.received_client = ttk.Label(self.server_frame, text="Received message from client:").grid(column=0,row=5,sticky=tk.W, padx=20,pady=0)
        self.received_client_entry = tk.Text(self.server_frame ,width=20,height=3) 
        self.received_client_entry.grid(column=0 ,row=6 ,sticky= EW,padx=20,pady=5, columnspan=2)

        #scrollbar - must be fixed
          # scrollbar = ttk.Scrollbar(server_frame, orient='vertical', command=received_client_entry.yview)
        # scrollbar.grid(row=6, column=1, sticky=tk.E)
        # received_client_entry['yscrollcommand'] = scrollbar.set
        #scrollbar - must be fixed

        self.delete_button_server = tk.Button(self.server_frame, text="DELETE", background="#eb3838", foreground="white")
        self.delete_button_server.grid(column=1, row=7, sticky=E, pady=5, padx=20)
        self.delete_button_server.bind("<Button-1>", server.delete_entry)

        self.send_client = ttk.Label(self.server_frame, text="Send message to client:").grid(column=0,row=8, sticky=tk.W, padx=20,pady=15)
        self.send_client_entry = tk.Text(self.server_frame, width=20, height=3)
        self.send_client_entry.grid(column=0,row=9,sticky=tk.EW, padx=20,pady=0, columnspan=2)

        self.send_button = tk.Button(self.server_frame, text="SEND", background="#278c3d", foreground="white")
        self.send_button.grid(column=1, row=10, sticky=E, pady=5, padx=20)
        self.send_button.bind("<Button-1>", server.send_message_to_client)
        print(  "serverWidgets completed\n")
        



       
