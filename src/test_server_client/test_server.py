#pylint: skip-file
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('localhost', 50000))
# s.listen(1)
# conn, addr = s.accept()
# while 1:
#     data = conn.recv(1024)
#     print(data)
#     if data == '!!':
#         break
#     conn.sendall(data)
# conn.close()

import select, socket, sys, queue
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 50000))
server.listen(5)
inputs = [server]
outputs = []
message_queues = {}

print(server)
print(inputs)
while inputs:
    print("while")
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs) #conn gelene kadar program burda duruyo
    print(readable)
    print(writable)
    print(exceptional)
    for s in readable:
        print("readable")
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
        else:
            print("readable else")
            data = s.recv(1024)
            print(data)
            if data:
                print("readable else if")
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print("readable else else")
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writable:
        print("writable")
        try:
            print("try")
            next_msg = message_queues[s].get_nowait()
            print(next_msg)
        except queue.Empty:
            print("except")
            outputs.remove(s)
        else:
            print("writable else")
            s.send(next_msg)

    for s in exceptional:
        print("excepton")
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]