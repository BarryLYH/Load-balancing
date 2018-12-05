import socket
import random

queue = []

host_ser = ['', 
            '172.31.16.50',  '172.31.16.34',  '172.31.31.59',  '172.31.23.153', '172.31.19.225',
            '172.31.21.186', '172.31.23.13',  '172.31.20.220', '172.31.23.212', '172.31.24.224',
            '172.31.22.198', '172.31.20.22',  '172.31.19.173', '172.31.24.209', '172.31.19.235',
            '172.31.29.129', '172.31.27.56',  '172.31.20.140', '172.31.25.205', '172.31.29.39',
            '172.31.26.187', '172.31.20.147', '172.31.28.16',  '172.31.23.37',  '172.31.22.52',
            '172.31.18.15',  '172.31.17.215', '172.31.29.155', '172.31.22.136', '172.31.28.119',
            '172.31.18.220', '172.31.21.30',  '172.31.23.145', '172.31.20.185', '172.31.24.72',
            '172.31.24.144', '172.31.22.6',   '172.31.27.171', '172.31.22.152', '172.31.30.199',
            '172.31.28.54',  '172.31.21.190', '172.31.25.196', '172.31.30.207', '172.31.24.140',
            '172.31.31.65',  '172.31.26.6',   '172.31.18.24',  '172.31.22.67',  '172.31.22.12']

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
