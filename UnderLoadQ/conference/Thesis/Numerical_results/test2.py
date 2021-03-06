from pylab import *
import matplotlib.pyplot as plt

name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
num_list = [1.5, 0.6, 7.8, 6]
num_list1 = [1, 2, 3, 1]
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num_list, width=width, label='boy', fc='y')
for i in range(len(x)):
    x[i] = x[i] + width

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'style': 'italic',
         'size': 100}
plt.bar(x, num_list1, width=width, label='d', tick_label=name_list, fc='r')
plt.legend(prop = font1)
plt.show()