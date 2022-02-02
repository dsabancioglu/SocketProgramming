#pylint: skip-file
import threading

from src.socket.client import Client
from src.socket.server import Server
from src.window.root import root

server = Server()
client = Client() 

if client.clientWidgets.created and server.serverWidgets.created :
    root.mainloop()

client_get_message_thread = threading.Thread(target=client.get_message, args=(0,))
server_get_message_thread = threading.Thread(target=server.get_message, args=(0,))

