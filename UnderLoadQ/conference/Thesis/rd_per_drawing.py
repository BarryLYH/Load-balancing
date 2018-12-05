import numpy as np
import matplotlib.pyplot as plt

t_pod202 = 1.381135395
t_pod204 = 1.26952321079
t_pod1002 = 1.12268490225
t_pod1004 = 1.09963391402

t_ne202 = 1.28938766532
t_ne204 = 1.03310835621
t_ne1002 = 1.03272555811
t_ne1004 = 1.000207134

t_e202 = 1.57322784258
t_e204 = 1.46068819273
t_e1002 = 1.09463720422
t_e1004 = 1.04918107932

t_pod = [1.381135395, 1.26952321079, 1.12268490225, 1.09963391402]
t_ne = [1.28938766532, 1.03310835621, 1.03272555811, 1.000207134]
t_e = [1.57322784258, 1.46068819273, 1.09463720422, 1.04918107932]

t_202 = np.array([1.381135395, 1.28938766532, 1.57322784258])
t_204 = np.array([1.26952321079, 1.03310835621, 1.46068819273])
t_1002 = np.array([1.12268490225, 1.03272555811, 1.09463720422])
t_1004 = np.array([1.09963391402, 1.000207134, 1.049181079325])

names= ['JIQ-Pod', 'JIQ-NE', 'JIQ-E']
width = 0.2

ind=np.arange(len(names))
plt.bar(ind, t_202, width, label='r=20,d=2', color='w',hatch='....')
plt.bar(ind+width, t_204, width, label='r=20,d=4', color='w')
plt.bar(ind+width*2, t_1002, width, label='r=100,d=2', color='w', hatch='/////')
plt.bar(ind+width*3, t_1004, width, label='r=100,d=4', color='w', hatch = '\\\\')

for a,b in zip(ind, t_202):
    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')

for a,b in zip(ind+width, t_204):
    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')

for a,b in zip(ind+width*2, t_1002):
    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')

for a,b in zip(ind+width*3, t_1004):
    plt.text(a+0.09, b, '%.2f' % b, ha ='center', va='bottom')

plt.ylabel("Mean Response Time (s)",fontsize=15)
plt.ylim(1,1.6)
plt.xticks(ind+2*width,("JIQ-Pod","JIQ-NE","JIQ-E"),fontsize=15)
plt.legend(loc='best')

plt.show()

