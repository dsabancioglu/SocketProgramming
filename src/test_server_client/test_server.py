#pylint: skip-file
import socket
import sys

#bunlari bosver sen server accepti client'ta hallet, bir de öyle dene

class TestServer:
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 12345
        s.bind(('0.0.0.0', port))
        print ('Socket binded to port 12345')
        s.listen(3)
        print ('socket is listening')

        
        c, addr = s.accept()
        print ('Got connection from ', addr)
        print (c.recv(1024))
        c.close() 