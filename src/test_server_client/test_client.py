#pylint: skip-file
import socket

class TestClient:
    def __init__(self):
        s = socket.socket()
        port = 12345
        s.connect(('localhost', port))

        while True:
            receivedMessage =s.recv(1024)
            print(receivedMessage)
            s.close()
  
