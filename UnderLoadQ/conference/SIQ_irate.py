import random
import simpy
import numpy as np
from collections import deque


def system_input():
    # return 0.008
    return np.random.exponential(1/ (load * servers_num))


def server_worktime():
    # k = np.random.multinomial(1, [.99, .01])   # Bimodal-2
    # return k[0] + k[1] * 101
    # return 1 / 3 * np.random.weibull(1 / 3)   #Weibull-2
    # return np.random.weibull(0.5)     #Weibull-1
    # k = np.random.multinomial(1, [.9 ,  .1])   # Bimodal-1
    # return k[0]+k[1]*11
    return np.random.exponential(1)  # Exponential
    # return 2


def jiq_run(env, server, line, servers_num, ique_num, d):
    number=0
    while number<=(servers_num * 500):
        number+=1
        if (number % 5000 == 0) and (number>100000):
            counter = 0
            for ll in range(1, ique_num + 1):
                if len(iquene[ll]) == 0:
                    counter += 1
            ra.append(counter)
        yield env.timeout(system_input())
        randnum = random.randint(1, ique_num)
        if len(iquene[randnum]) == 0:
            ser_num = random.randint(1, servers_num)
        else:
            ser_num = iquene[randnum][0]
            for i in range(len(iquene[randnum]) - 1):
                iquene[randnum][i] = iquene[randnum][i + 1]
            iquene[randnum].pop()
        env.process(dispatch(env, number, server[ser_num], ser_num, line, ique_num, d))


def dispatch(env, number, server, ser_num, line, ique_num, d):
    with server.request() as req:
        time_begin = env.now
        line[ser_num] += 1
        yield req
        #print(env.now, 'server{} processes Packet{}'.format(ser_num, number))
        yield env.timeout(server_worktime())
        line[ser_num] -= 1
        if line[ser_num] == 0:
            for i in range(d+1):
                if i < d:
                    qnum = random.randint(1, ique_num)
                    if len(iquene[qnum]) == 0:
                        iquene[qnum].append(ser_num)
                        break
                else:
                    qnum = random.randint(1, ique_num)
                    iquene[qnum].append(ser_num)

def avemechine(time):
    length = len(time)
    sum = 0
    kk = 0
    for i in range(length):
        kk += 1
        sum = sum + time[i]
    return (sum / kk)


outfile = open('/users/barry/Desktop/SIQ_rate.txt', 'w')

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
env = simpy.Environment()

ique_line = [1000]
r_line = [10]
d_line = [2]

for ique_num in ique_line:
    for r in r_line:
        for d in d_line:
            servers_num = ique_num * r
            outfile.write('Queue Number: {}    Server Number: {}   d:{}'.format(ique_num, servers_num, d))
            outfile.write('\n')

            print('Queue Number: {}    Server Number: {}  d:{}\n'.format(ique_num, servers_num, d))


            rate_rec = []
            load = 0.90
            while load < 1:
                if load < 0.95:
                    load += 0.05
                else:
                    load += 0.01
                rate = []
                #for accurate_counter in range(5):
                ra = []
                line = [0 for i in range(servers_num + 1)]
                iquene = deque([] for i in range(ique_num + 1))
                for i in range(1, ique_num + 1):
                    randnum_in = random.randint(1, ique_num)
                    iquene[randnum_in].append(i)
                server = {}
                for i in range(1, servers_num + 1):
                    server[i] = simpy.Resource(env, 1)

                env.process(jiq_run(env, server, line, servers_num, ique_num, d))
                env.run()
                rate.append(avemechine(ra) / ique_num)

                rate_rec.append(avemechine(rate))
                print('load =', load, 'rate =', rate_rec[-1])

            outfile.write('\n')
            outfile.write('{}'.format(rate_rec))
            outfile.write('\n')

outfile.close()
