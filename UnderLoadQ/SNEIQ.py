import random
import simpy
import numpy as np
from collections import deque

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

def jiq_run(env, server, line, numser):
    number=0
    while number<=(numser * 500):
        number += 1
        yield env.timeout(system_input())
        qnum1 = random.randint(1, ique_num)
        qnum2 = random.randint(1, ique_num)
        while qnum1 == qnum2:
            qnum2 = random.randint(1, ique_num)
        if len(iquene[qnum1]) == 0:
            randnum = qnum2
        else:
            randnum = qnum1
        if len(iquene[randnum]) == 0:
            ser_num = random.randint(1, servers_num)
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

def avemechine(time):
    length = len(time)
    sum = 0
    kk = 0
    for i in range(int(length*0.2), int(length*0.8)):
        kk += 1
        sum = sum + time[i]
    return (sum / kk)

##########################   MAIN CODE   ###############################

outfile = open('/UBC-O/barrylyh/Desktop/SNEIQ.txt', 'w')

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
env = simpy.Environment()

ique_line = [10, 100, 1000]
r_line = [5, 10, 20]

for ique_num in ique_line:
    for r in r_line:
        servers_num = ique_num * r
        outfile.write('Queue Number: {}    Server Number: {}'.format(ique_num, servers_num))
        print('Queue Number: {}    Server Number: {} \n'.format(ique_num, servers_num))
        outfile.write('\n')

        load_rec = []
        load = 0.495
        while load < 1:
            load += 0.005
            storer = []
            for accurate_counter in range(10):
                time = []
                line = [0 for i in range(servers_num+1)]
                iquene = deque([] for i in range(ique_num+1))
                for i in range(1, ique_num+1):
                    randnum_in = random.randint(1, ique_num)
                    iquene[randnum_in].append(i)
                server = {}
                for i in range(1, servers_num+1):
                    server[i]= simpy.Resource(env, 1)

                env.process(jiq_run(env, server, line, servers_num))
                env.run()

                storer.append(avemechine(time))

            storer.sort()
            load_rec.append(avemechine(storer))

        outfile.write('\n')
        outfile.write('{}'.format(load_rec))
        outfile.write('\n')
        outfile.write('\n')
outfile.close()
