#pylint: skip-file
from tkinter import *
from tkinter import ttk
import tkinter as tk
import socket


root = Tk()
root.title("Client Server Communication")
root.geometry('900x500+500+250')

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

    def send_message_to_client(self,event):
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

server = Server()

#--------------------------------------------------------------------

class Client:
    def __init__(self):
        self.ip_var = StringVar()
        self.port_var = StringVar()
        self.socket = socket.socket()

    def get_connection(self,event):
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

    def send_message_to_server(self,event):
        message = send_server_entry.get('1.0','end').encode()
        print(message)
        self.socket.send(message)

    def get_message(self,event):
        self.receivedMessage = self.socket.recv(1024)
        received_server_entry.insert(1.0,self.receivedMessage)

    def close_connection(self):
        self.socket.close()
        print("closed")
        
    def delete_entry(self,event):
        received_server_entry.delete('1.0', END)


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
listen_button.bind("<Button-1>", server.bind)

server_status = ttk.Label(server_frame, text="Server Status:").grid(column=0,row=4, sticky=tk.W, padx=20,pady=20)
server_status_value = ttk.Label(server_frame, text="Stop", foreground="red")
server_status_value.grid(column=1,row=4, sticky=tk.EW, padx=20,pady=20) #listen buttonu nurayı triggerlicak

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
delete_button_server.bind("<Button-1>", server.delete_entry)

send_client = ttk.Label(server_frame, text="Send message to client:").grid(column=0,row=8, sticky=tk.W, padx=20,pady=15)
send_client_entry = tk.Text(server_frame, width=20, height=3)
send_client_entry.grid(column=0,row=9,sticky=tk.EW, padx=20,pady=0, columnspan=2)

send_button = tk.Button(server_frame, text="SEND", background="#278c3d", foreground="white")
send_button.grid(column=1, row=10, sticky=E, pady=5, padx=20)
send_button.bind("<Button-1>", server.send_message_to_client)
send_button.bind("<Button-1>", client.get_message, add='+')




#CLIENT widgets
client_label = ttk.Label(client_frame, text="Client")
client_label.grid(column=0, row=0, sticky=tk.E, padx=5 ,pady=5)

client_ip = ttk.Label(client_frame, text="Ip:").grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
client_ip_entry = ttk.Entry(client_frame, textvariable=client.ip_var).grid(column=1, row=1, sticky=tk.W, padx=20,pady=5)

client_port = ttk.Label(client_frame, text="Port:").grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
client_port_entry = ttk.Entry(client_frame,textvariable=client.port_var).grid(column=1, row=2, sticky=tk.W, padx=20, pady=5)

connect_button = tk.Button(client_frame, text="Connect Server",background="#54727a",foreground="white")
connect_button.grid(column=1, row=3, sticky=tk.NS, padx=20, pady=5) #is active i triggerlaması lazım event bind edicez
connect_button.bind("<Button-1>", client.get_connection)

connection_statement = ttk.Label(client_frame, text="Connection Statement:").grid(column=0,row=4, sticky=tk.W, padx=20,pady=20)
connection_statement_value = ttk.Label(client_frame, text="Not connected", foreground="red")
connection_statement_value.grid(column=1,row=4, sticky=tk.EW, padx=20,pady=20)

send_server = ttk.Label(client_frame, text="Send message to server:").grid(column=0,row=5, sticky=tk.W, padx=20,pady=0)
send_server_entry = tk.Text(client_frame, width=20, height=3)
send_server_entry.grid(column=0,row=6,sticky=tk.EW, padx=20,pady=5, columnspan=2)

send_button_client = tk.Button(client_frame, text="SEND", background="#278c3d", foreground="white")
send_button_client.grid(column=1, row=7, sticky=E, pady=5, padx=20)
send_button_client.bind("<Button-1>", client.send_message_to_server)
send_button_client.bind("<Button-1>", server.get_message, add='+')

received_server = ttk.Label(client_frame, text="Received message from Server:").grid(column=0,row=8,sticky=tk.W, padx=20,pady=15)
received_server_entry = tk.Text(client_frame, width=20,height=3) 
received_server_entry.grid(column=0 ,row=9 ,sticky= EW,padx=20,pady=0, columnspan=2)

delete_button_client = tk.Button(client_frame, text="DELETE", background="#eb3838", foreground="white")
delete_button_client.grid(column=1, row=10, sticky=E, pady=5, padx=20)
delete_button_client.bind("<Button-1>", client.delete_entry)

 
root.mainloop()




