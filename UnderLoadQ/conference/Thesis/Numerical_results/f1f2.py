import matplotlib.pyplot as plt

x = 0.001
x_line = []
f1_line = []
f2_line = []
r=1
d=2
l = 0.5

while x < 1:
    '''
    k = 0
    for i in range(1, 50):
        upper = (r ** i) * (1 - l * (x)) ** i
        lower = 1
        for j in range(1, i + 1):
            lower = lower * (r + j * (x))
        k = k + upper / lower * x
    result1 = k + x
    f1_line.append(result1)

'''
    k = 0
    for i in range(1, 50):
        o = (d - 1) * (i - 1)
        up = (r ** i) * ((1 - (l * x)) ** i) * ((1 - x) ** o)
        low = 1
        for j in range(1, i + 1):
            low = low * (r + j * x)
        k = k + up / low * (1 - (1 - x) ** d)
    result2 = k + x
    f2_line.append(result2)

    x_line.append(x)
    x += 0.001


#plt.plot(x_line, f1_line, label= 'JIQ')
plt.plot(x_line, f2_line, label='E')
plt.legend('best')
plt.show()