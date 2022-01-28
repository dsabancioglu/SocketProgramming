#pylint: skip-file
from server import Server
from client import Client
from root import *

server = Server()
client = Client(server) 

server.create_widgets(server, client)
client.create_widgets(server, client)

if client.created and server.created :
    root.mainloop()


