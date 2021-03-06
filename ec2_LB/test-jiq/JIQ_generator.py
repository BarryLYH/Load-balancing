import socket
import random
import time
import numpy as np

NUM = 100
load = 0.9


host_iq = ['', '172.31.26.162', '172.31.31.108']

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

N = 4 # Number of servers

for i in range(NUM):
    line = str(i + 1) + ' ' + str(timein()) + ' ' + str(processtime())
    d = randpick(len(host_iq))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_iq[d], 8000))

    print(line)
    s.send(line.encode('utf-8'))
    s.close()

    time.sleep(arrivalwait())


