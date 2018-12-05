import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

names = ('JIQ-E', 'JIQ-NE', 'JIQ-Pod', 'JIQ')
y_pos = np.arange(len(names))
performance = [2.42323388662, 1.88812454657,2.00255083399, 2.77428427396]

plt.barh(y_pos, performance,  align='center', height = 0.5, alpha=0.4)
plt.yticks(y_pos, names)
plt.xlabel('Mean Response Time(s)')

plt.show()
#plt.savefig("/users/barry/desktop/ec2.eps",format="eps")