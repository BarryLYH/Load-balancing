import socket
import random
import time
import numpy as np

NUM = 50000
load = 0.9


host_iq = ['', '172.31.22.40',  '172.31.26.234', '172.31.20.192', '172.31.25.13',  '172.31.24.182',]


def timein():
    return time.time()

def processtime():
    return np.random.exponential(1)

def arrivalwait():
    return np.random.exponential(1)/(load * N)

def randpick(N):
    return random.randint(1, N-1)

def pod(d1, d1_num, d2, d2_num):
    if d1_num > d2_num:
        return [d1, d1_num]
    else:
        return [d2, d2_num]

N = 50

for i in range(NUM):

    line =str(i+1) + ' ' + str(timein()) + ' ' + str(processtime())

    mess = 'Request length'
    d1 = randpick(len(host_iq))
    d2 = randpick(len(host_iq))

    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host_iq[d1], 8000))
    # s.connect((host[d1], port[d1]))
    s1.send(mess.encode('utf-8'))
    reply = s1.recv(1024)
    d1_num = int(reply.decode('utf-8'))
    print('Idel_Queue {} has {} task'.format(d1, d1_num))
    s1.close()

    if d1_num > 0:
        d = d1
        print('Choose i-queue', d1)
    else:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.connect((host_iq[d2], 8000))
        # s.connect((host[d1], port[d1]))
        s1.send(mess.encode('utf-8'))
        reply = s1.recv(1024)
        d2_num = int(reply.decode('utf-8'))
        print('Idel_Queue {} has {} task'.format(d2, d2_num))
        s1.close()

        if d1_num < d2_num:
            d = d2
            print('Choose i-queue', d2)
        else:
            d = d1
            print('Choose i-queue', d1)

    idle_need = 'Idle server'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_iq[d], 8000))

    print(line)
    s.send(line.encode('utf-8'))
    s.close()

    time.sleep(arrivalwait())


