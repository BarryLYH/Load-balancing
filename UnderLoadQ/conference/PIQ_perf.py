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

def jiq_run(env, server, line, servers_num, ique_num, d):
    number=0
    while number<=(servers_num * 500):
        number+=1
        yield env.timeout(system_input())
        for i in range(d+1):
            if i < d:
                qnum = random.randint(1, ique_num)
                cost[0] += 1
                if len(iquene[qnum]) > 0:
                    ser_num = iquene[qnum][0]
                    for j in range(len(iquene[qnum]) - 1):
                        iquene[qnum][j] = iquene[qnum][j + 1]
                    iquene[qnum].pop()
                    break
            else:
                ser_num = random.randint(1, servers_num)
        env.process(dispatch(env, number, server[ser_num], ser_num, line, ique_num))

def dispatch(env, number, server, ser_num, line, ique_num):
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
    for i in range(length):
        kk += 1
        sum = sum + time[i]
    return (sum / kk)

##########################   MAIN CODE   ###############################

outfile = open('/users/barry/Desktop/PIQ.txt', 'w')

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
env = simpy.Environment()

ique_line = [500]
r_line = [20]
d_line = [2, 4]

for ique_num in ique_line:
    for r in r_line:
        for d in d_line:
            servers_num = ique_num * r
            outfile.write('Queue Number: {}    Server Number: {}'.format(ique_num, servers_num))
            print('Queue Number: {}    Server Number: {} \n'.format(ique_num, servers_num))

            outfile.write('\n')

            load_rec = []
            cost_rec = []
            load = 0.45
            while load < 1:
                if load<0.95:
                    load += 0.05
                else:
                    load += 0.01
                storer = []
                cost_list = []
                #for accurate_counter in range(5):
                time = []
                cost = [0]
                line = [0 for i in range(servers_num+1)]
                iquene = deque([] for i in range(ique_num+1))
                for i in range(1, ique_num+1):
                    randnum_in = random.randint(1, ique_num)
                    iquene[randnum_in].append(i)
                server = {}
                for i in range(1, servers_num+1):
                    server[i]= simpy.Resource(env, 1)

                env.process(jiq_run(env, server, line, servers_num, ique_num, d))
                env.run()

                storer.append(avemechine(time[int(len(time)/2):]))
                cost_list.append(cost[0])

                storer.sort()
                load_rec.append(avemechine(storer))
                cost_rec.append(avemechine(cost_list))
                print('d={} load={} time={} cost={}'.format(d, load, load_rec[-1], cost_list[-1]))
                print(load_rec)
                print(cost_rec)

            outfile.write('\n')
            outfile.write('{}'.format(load_rec))
            outfile.write('\n')
            outfile.write('{}'.format(cost_rec))
            outfile.write('\n')
            outfile.write('\n')

outfile.close()

