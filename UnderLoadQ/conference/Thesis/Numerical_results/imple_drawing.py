import numpy as np
import matplotlib.pyplot as plt


c = [2.77428427396, 2.00255083399, 1.88812454657, 2.42323388662]
names= ['JIQ', 'JIQ-Pod', 'JIQ-NE', 'JIQ-E']
width = 0.5

ind=np.arange(len(names))
plt.bar(ind+width, c, width, label='r=20,d=2', color='coral1')

#for a,b in zip(ind, c):
#    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')

plt.ylabel("Mean Reponse Time(s)",fontsize=15)
#plt.ylim(1,1.6)
plt.xticks(ind+0.7,('JIQ',"JIQ-Pod","JIQ-NE","JIQ-E"),fontsize=15)
#plt.legend(loc='upper left')

plt.show()