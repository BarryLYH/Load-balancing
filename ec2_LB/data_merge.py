import numpy as np

path = '/users/barry/desktop/ec2_results/'


file_path = path + 'e' + '.txt'

infile  = open(file_path, 'r')
data = infile.readlines()
infile.close()

rt = []

for line in data:
    line = line.strip('\n')
    time = line.split()
    rt.append(float(time[3])-float(time[1]))

print(np.mean(rt))