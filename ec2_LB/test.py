
import time
import numpy as np


def timein():
    return time.time()

def processtime():
    return np.random.exponential(1)

i = 0
while True:
    i += 1
    line = str(i + 1) + ' ' + str(timein()) + ' ' + str(processtime())
    print(line)
    num_task = line.split()[0]
    timein = float(line.split()[1])
    timewait = float(line.split()[2])
