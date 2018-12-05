import random
import simpy
import numpy as np
from collections import deque

RANDOM_SEED = 42
ique_num = 50
r = 10
servers_num = ique_num * r
load = 0.99

def system_input():
    #return 0.008
    return np.random.exponential(1/(load * servers_num) )

def server_worktime():
    #k = np.random.multinomial(1, [.99, .01])   # Bimodal-2
    #return k[0] + k[1] * 101
    #return 1 / 3 * np.random.weibull(1 / 3)   #Weibull-2
    #return np.random.weibull(0.5)     #Weibull-1
    #k = np.random.multinomial(1, [.9 ,  .1])   # Bimodal-1
    #return k[0]+k[1]*11
    return np.random.exponential(1)   #Exponential
    #return 2


def jiq_run(env, server, line, ifInQ):
    number=0
    cutnum = 100000
    downnum = 150000
    while number<=200000:
        number += 1
        yield env.timeout(system_input())
        randnum = random.randint(1,ique_num)
        if len(iquene[randnum]) == 0:
            ser_num = random.randint(1,servers_num)
            if ifInQ[ser_num] > 0:
                iquene[ifInQ[ser_num]].remove(ser_num)
                ifInQ[ser_num] = 0
        else:
            ser_num = iquene[randnum][0]
            iquene[randnum].remove(ser_num)
            ifInQ[ser_num] = 0
            #for i in range(len(iquene[randnum]) - 1):
            #    iquene[randnum][i] = iquene[randnum][i + 1]
            #iquene[randnum].pop()
        line[ser_num] += 1
        env.process(dispatch(env, number, server[ser_num], ser_num, line, ifInQ))

        if number == 150000:

            for i in range(1, ique_num+1):
                outfile.write('Queue{} has {}'.format(i, iquene[i]))
                outfile.write('\n')

            for i in range(1, servers_num+1):
                outfile.write('Server{} has {}'.format(i, line[i]))
                outfile.write('\n')

        if (number == cutnum) and (number <= downnum):
            cutnum += 1000
            for i in range(1, servers_num+1):
                lengthRecord[i].append(line[i])



def dispatch(env, number, server, ser_num, line, ifInQ):
    with server.request() as req:
        lineTimeIn = line[ser_num]
        time_begin = env.now
        #print(env.now, 'Packet{} sent to server{}'.format(number, ser_num))
        yield req
        #print(env.now, 'server{} processes Packet{}'.format(ser_num, number))
        yield env.timeout(server_worktime())
        time_end = env.now
        time.append(time_end - time_begin)
        #print(env.now,'Packet{} finished and left server{}'.format(number,ser_num))
        line[ser_num] -= 1
        lineTimeOut = line[ser_num]
        differ = lineTimeOut - lineTimeIn

        if ((line[ser_num] == 0) or (differ < 0)) and (ifInQ[ser_num] == 0):
            JoinQ_num = random.randint(1,ique_num)
            iquene[JoinQ_num].append(ser_num)
            ifInQ[ser_num] = JoinQ_num


outfile = open('/users/barry/desktop/record1.txt', 'w')

np.random.seed(RANDOM_SEED)
env = simpy.Environment()

lengthRecord = [[] for i in range(servers_num+1)]
time = []
line = [0 for i in range(servers_num+1)]
ifInQ = [0 for i in range(servers_num+1)]
iquene = deque([] for i in range(ique_num+1))
for i in range(1, servers_num+1):
    randnum_in = random.randint(1, ique_num)
    iquene[randnum_in].append(i)
    ifInQ[i] = randnum_in


server = {}
for i in range(1, servers_num+1):
    server[i]= simpy.Resource(env, 1)


env.process(jiq_run(env, server, line, ifInQ))
env.run()

sum = 0
kk=0

for i in range(int(len(time)/2), len(time)):
    kk+=1
    sum = sum + time[i]
ave = sum / kk
print('The average time:', ave)

for i in range(1, servers_num+1):
    kk = 0
    sum = 0
    for j in range(0, len(lengthRecord[i])):
        kk+=1
        sum = sum + lengthRecord[i][j]
    outfile.write('MeanLength of Q{} is {}'.format(i,sum/kk))
    outfile.write('\n')
outfile.close()