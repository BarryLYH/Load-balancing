import socket
import random

queue = []

host_ser = ['', '172.31.30.217', '172.31.31.216', '172.31.21.40', '172.31.21.119',]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8000))
s.listen(5)

while True:
    connection, address = s.accept()
    print('Receive message')
    while True:
        indata = connection.recv(1024)
        data = indata.decode('utf-8')
        print(data,'\n')

        if not data: break

        if data == 'Join Queue':
            print('Idle server adding')
            add = str(address)
            add = add.split()[0]
            add = add[2: -2]
            queue.append(add)
            print(len(queue))
        else:
            if len(queue) == 0:
                d = random.randint(1, len(host_ser) - 1)
                ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ss.connect((host_ser[d], 8000))
                print('task to', d, len(queue), '\n')
                ss.send(data.encode('utf-8'))
                ss.close()
            else:
                add = queue[0]
                queue.pop(0)
                print('Send to Idle Server\n')
                ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ss.connect((add, 8000))
                ss.send(data.encode('utf-8'))
                ss.close()

    connection.close()
