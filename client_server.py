#pylint: skip-file
from tkinter import *
from tkinter import ttk
import tkinter as tk

from client_ import Client
from server_ import Server

root = Tk()
root.title("Client Server Communication")
root.geometry('900x500+500+250')

server = Server()
client = Client()

#Server frame
server_frame = ttk.Frame(root)
server_frame.columnconfigure(0, weight=1)
server_frame.columnconfigure(1, weight=1)
server_frame.pack(fill=BOTH, side=LEFT ,expand=True)

#Client Frame
client_frame = ttk.Frame(root)
client_frame.columnconfigure(0, weight=1)
client_frame.columnconfigure(1, weight=1)
client_frame.pack(fill=BOTH, side=RIGHT , expand=True)

#SERVER widgets
server_label = ttk.Label(server_frame, text="Server")
server_label.grid(column=0, row=0, sticky=tk.E, padx=5 ,pady=5)

server_ip = ttk.Label(server_frame, text="Ip:").grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
server_ip_entry = ttk.Entry(server_frame, textvariable=server.ip_var).grid(column=1, row=1, sticky=tk.W, padx=20,pady=5)

server_port = ttk.Label(server_frame, text="Port:").grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
server_port_entry = ttk.Entry(server_frame, textvariable=server.port_var).grid(column=1, row=2, sticky=tk.W, padx=20, pady=5)

listen_button = tk.Button(server_frame, text="Run Server",background="#54727a",foreground="white")
listen_button.grid(column=1, row=3, sticky=tk.NS, padx=20, pady=5)


server_status = ttk.Label(server_frame, text="Server Status:").grid(column=0,row=4, sticky=tk.W, padx=20,pady=20)
server_status_value = ttk.Label(server_frame, text="Stop", foreground="red")
server_status_value.grid(column=1,row=4, sticky=tk.EW, padx=20,pady=20) 


received_client = ttk.Label(server_frame, text="Received message from client:").grid(column=0,row=5,sticky=tk.W, padx=20,pady=0)
received_client_entry = tk.Text(server_frame ,width=20,height=3) 
received_client_entry.grid(column=0 ,row=6 ,sticky= EW,padx=20,pady=5, columnspan=2)

#scrollbar - must be fixed
scrollbar = ttk.Scrollbar(server_frame, orient='vertical', command=received_client_entry.yview)
scrollbar.grid(row=6, column=1, sticky=tk.E)
received_client_entry['yscrollcommand'] = scrollbar.set
#scrollbar - must be fixed

delete_button_server = tk.Button(server_frame, text="DELETE", background="#eb3838", foreground="white")
delete_button_server.grid(column=1, row=7, sticky=E, pady=5, padx=20)


send_client = ttk.Label(server_frame, text="Send message to client:").grid(column=0,row=8, sticky=tk.W, padx=20,pady=15)
send_client_entry = tk.Text(server_frame, width=20, height=3)
send_client_entry.grid(column=0,row=9,sticky=tk.EW, padx=20,pady=0, columnspan=2)

send_button = tk.Button(server_frame, text="SEND", background="#278c3d", foreground="white")
send_button.grid(column=1, row=10, sticky=E, pady=5, padx=20)

#server button bind
listen_button.bind("<Button-1>", lambda event : server.bind(event, server_status_value= server_status_value))
delete_button_server.bind("<Button-1>", lambda event,m=received_client_entry: server.delete_entry(m))
send_button.bind("<Button-1>", lambda event ,m= send_client_entry :server.send_message_to_client(m))
send_button.bind("<Button-1>", lambda event ,m= received_client_entry: client.get_message(m), add='+')

listen_button.focus_set()
delete_button_server.focus_set()
send_button.focus_set()

#--------------------------------------------------------------------
#CLIENT widgets
client_label = ttk.Label(client_frame, text="Client")
client_label.grid(column=0, row=0, sticky=tk.E, padx=5 ,pady=5)

client_ip = ttk.Label(client_frame, text="Ip:").grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
client_ip_entry = ttk.Entry(client_frame, textvariable=client.ip_var).grid(column=1, row=1, sticky=tk.W, padx=20,pady=5)

client_port = ttk.Label(client_frame, text="Port:").grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
client_port_entry = ttk.Entry(client_frame,textvariable=client.port_var).grid(column=1, row=2, sticky=tk.W, padx=20, pady=5)

connect_button = tk.Button(client_frame, text="Connect Server",background="#54727a",foreground="white")
connect_button.grid(column=1, row=3, sticky=tk.NS, padx=20, pady=5) 

connection_statement = ttk.Label(client_frame, text="Connection Statement:").grid(column=0,row=4, sticky=tk.W, padx=20,pady=20)
connection_statement_value = ttk.Label(client_frame, text="Not connected", foreground="red")
connection_statement_value.grid(column=1,row=4, sticky=tk.EW, padx=20,pady=20)


send_server = ttk.Label(client_frame, text="Send message to server:").grid(column=0,row=5, sticky=tk.W, padx=20,pady=0)
send_server_entry = tk.Text(client_frame, width=20, height=3)
send_server_entry.grid(column=0,row=6,sticky=tk.EW, padx=20,pady=5, columnspan=2)

send_button_client = tk.Button(client_frame, text="SEND", background="#278c3d", foreground="white")
send_button_client.grid(column=1, row=7, sticky=E, pady=5, padx=20)



received_server = ttk.Label(client_frame, text="Received message from Server:").grid(column=0,row=8,sticky=tk.W, padx=20,pady=15)
received_server_entry = tk.Text(client_frame, width=20,height=3) 
received_server_entry.grid(column=0 ,row=9 ,sticky= EW,padx=20,pady=0, columnspan=2)


delete_button_client = tk.Button(client_frame, text="DELETE", background="#eb3838", foreground="white")
delete_button_client.grid(column=1, row=10, sticky=E, pady=5, padx=20)



connect_button.bind("<Button-1>", lambda event,m= connection_statement_value: client.get_connection(m)) #
send_button_client.bind("<Button-1>", lambda event, m= send_server_entry : client.send_message_to_server(m)) #
send_button_client.bind("<Button-1>",lambda event, m= received_server_entry : server.get_message(m), add='+') #
delete_button_client.bind("<Button-1>", lambda event, m= received_server_entry: client.delete_entry(m))

connect_button.focus_set()
send_button_client.focus_set()
delete_button_client.focus_set()

root.mainloop()




