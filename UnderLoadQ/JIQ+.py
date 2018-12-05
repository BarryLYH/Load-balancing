import random
import simpy
import numpy as np
from collections import deque

RANDOM_SEED = 42
ique_num = 1000
r = 10
servers_num = ique_num * r
load = 0.995

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

def jiq_run(env, server, line):
    number=0
    while number<=2000000:
        number+=1
        yield env.timeout(system_input())
        qnum1 = random.randint(1,ique_num)
        qnum2 = random.randint(1,ique_num)
        while qnum1 == qnum2:
            qnum2 = random.randint(1, ique_num)
        if len(iquene[qnum1]) == 0:
            randnum = qnum2
        else:
            randnum = qnum1
        if len(iquene[randnum]) == 0:
            ser_num = random.randint(1,servers_num)
        else:
            ser_num = iquene[randnum][0]
            for i in range(len(iquene[randnum]) - 1):
                iquene[randnum][i] = iquene[randnum][i + 1]
            iquene[randnum].pop()
        env.process(dispatch(env, number, server[ser_num], ser_num, line))


def dispatch(env, number, server, ser_num, line):
    with server.request() as req:
        time_begin = env.now
        #print(env.now, 'Packet{} sent to server{}'.format(number, ser_num))
        line[ser_num] += 1
        yield req
        #print(env.now, 'server{} processes Packet{}'.format(ser_num, number))
        yield env.timeout(server_worktime())
        time_end = env.now
        time.append(time_end - time_begin)
        #print(env.now,'Packet{} finished and left server{}'.format(number,ser_num))
        line[ser_num] -= 1
        if line[ser_num] == 0:
            JoinQ_num = random.randint(1, ique_num)
            iquene[JoinQ_num].append(ser_num)



np.random.seed(RANDOM_SEED)
env = simpy.Environment()

time = []
line = [0 for i in range(servers_num+1)]
iquene = deque([] for i in range(ique_num+1))
for i in range(1, ique_num+1):
    randnum_in = random.randint(1, ique_num)
    iquene[randnum_in].append(i)


server = {}
for i in range(1, servers_num+1):
    server[i]= simpy.Resource(env, 1)


env.process(jiq_run(env, server, line))
env.run()

sum = 0
kk=0

for i in range(int(len(time)/2), len(time)):
    kk+=1
    sum = sum + time[i]
ave = sum / kk
print('The average time:', ave)
