import time
import threading
import socket
import random

def randpick(N):
    return random.randint(1, N-1)

def taskin(queue):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8000))
    s.listen(10)
    while True:
        connection, address = s.accept()
        while True:
            indata = connection.recv(1024)
            data = indata.decode('utf-8')
            if not data:
                break
            else:
                print('packet comes in')
                queue.append(data)
        connection.close()



def taskprocess(queue):
    outfile = open('E_output.txt', 'a+')
    while True:
        if len(queue)>0:
            data = queue[0]
            num_task = data.split()[0]
            timein = float(data.split()[1])
            timewait = float(data.split()[2])

            time.sleep(timewait)
            output = str(num_task) + ' ' + str(timein) + ' ' + str(timewait) + ' ' + str(time.time())
            print(output)

            outfile.write(output)
            outfile.write('\n')
            outfile.flush()
            queue.pop(0)
            if len(queue) == 0:
                ifneedjiq[0] = True
            else:
                ifneedjiq[0] = False

        elif ifneedjiq[0]:
            message = 'Request length'
            d1 = randpick(len(iq_list))
            d2 = randpick(len(iq_list))

            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s1.connect((iq_list[d1], 8000))
            # s.connect((host[d1], port[d1]))
            s1.send(message.encode('utf-8'))
            reply = s1.recv(1024)
            d1_num = int(reply.decode('utf-8'))
            print('Idel_Queue {} has {} task'.format(d1, d1_num))
            s1.close()

            if d1_num == 0:
                d = d1
                print('Choose i-queue', d1)
            else:
                s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s1.connect((iq_list[d2], 8000))
                # s.connect((host[d1], port[d1]))
                s1.send(message.encode('utf-8'))
                reply = s1.recv(1024)
                d2_num = int(reply.decode('utf-8'))
                print('Idel_Queue {} has {} task'.format(d2, d2_num))
                s1.close()

                if d1_num > d2_num:
                    d = d2
                    print('Choose i-queue', d2,)
                else:
                    d = d1
                    print('Choose i-queue', d1,)

            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s1.connect((iq_list[d], 8000))
            message = 'Join Queue'
            s1.send(message.encode('utf-8'))
            s1.close()
            ifneedjiq[0] = False


iq_list = ['','172.31.22.40',  '172.31.26.234', '172.31.20.192', '172.31.25.13',  '172.31.24.182']

queue = []
ifneedjiq = [True]

counter = [0]

threads = []
t1 = threading.Thread(target=taskin, args=(queue,))
threads.append(t1)
t2 = threading.Thread(target=taskprocess,  args=(queue,))
threads.append(t2)


if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('end')