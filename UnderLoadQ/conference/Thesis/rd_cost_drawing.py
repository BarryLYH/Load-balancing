import numpy as np
import matplotlib.pyplot as plt

c_pod202 = 8199474.28571
c_pod204 = 11210097.8571
c_pod1002 = 6320874.71429
c_pod1004 = 7545797.57143

c_ne202 = 6707427.78571
c_ne204 = 8505252.78571
c_ne1002 = 5750768.85714
c_ne1004 = 6446077.57143

c_e202 = 12161844.5714
c_e204 = 18623927.5
c_e1002 = 14040453.8571
c_e1004 = 22781133.2857



c_202 = np.array([8199474.28571, 6707427.78571, 12161844.5714])
c_204 = np.array([11210097.8571, 8505252.78571, 18623927.5])
c_1002 = np.array([6320874.71429, 5750768.85714, 14040453.8571])
c_1004 = np.array([7545797.57143, 6446077.57143, 22781133.2857])

names= ['JIQ-Pod', 'JIQ-NE', 'JIQ-E']
width = 0.2

ind=np.arange(len(names))
plt.bar(ind, c_202, width, label='r=20,d=2', color='w',hatch='....')
plt.bar(ind+width, c_204, width, label='r=20,d=4', color='w')
plt.bar(ind+width*2, c_1002, width, label='r=100,d=2', color='w', hatch='/////')
plt.bar(ind+width*3, c_1004, width, label='r=100,d=4', color='w', hatch = '\\\\')
'''
for a,b in zip(ind, c_202):
    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')

for a,b in zip(ind+width, c_204):
    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')

for a,b in zip(ind+width*2, c_1002):
    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')

for a,b in zip(ind+width*3, c_1004):
    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')
'''
plt.ylabel("Average Cost",fontsize=15)
#plt.ylim(1,1.6)
plt.xticks(ind+2*width,("JIQ-Pod","JIQ-NE","JIQ-E"),fontsize=15)
plt.legend(loc='upper left')

plt.show()