#pylint: skip-file
from http import client
from client import clientWidgets
from server import serverWidgets
from root import *

root = Root()
server = Server()
client = Client(server) #client baglanacagi server objesini aldi

if clientWidgets.widget_created == 1 and serverWidgets.widget_created ==1 :
    root.mainloop()


