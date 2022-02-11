#pylint: skip-file
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
for i in range(5):
    s.sendall('Hello, world')
    s.sendall('!!')
data = s.recv(1024)
print(data)
s.close()
#print ("Received {}".format(repr(data)))
  
