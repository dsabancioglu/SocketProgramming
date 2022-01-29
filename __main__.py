#pylint: skip-file
from src.socket.client import Client
from src.socket.server import Server
from src.window.root import root

server = Server()
client = Client(server) 

server.create_widgets(server, client)
client.create_widgets(server, client)

if client.created and server.created :
    root.mainloop()


