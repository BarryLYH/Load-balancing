import matplotlib.pyplot as plt

x = 0.5
y_all = 0
g_all = 0
y_line = [x]
g_line = [x]
aa_line = [0]
r=4
d=3
l = 0.9
y=x
g=x

for i in range(1, 50):
    #upper = (r) * (1 - l * (x ** d))
    #lower = (r * (1 - x ** d) / (1 - x) + i * (x ** d))
    upper = (r ** i) * (1 - l * (x ** d)) ** i
    lower = 1
    for j in range(1, i + 1):
        lower = lower * (r * (1 - x ** d) / (1 - x) + j * (x ** d))
    k =  upper / lower * x
    y = k
    up = r * (1-l*x)
    low = r + i*x
    g = up/low * g
    y_line.append(y)
    g_line.append(g)
    aa_line.append(i)
    y_all += y
    g_all += g

plt.plot(aa_line, y_line, label='y')
plt.plot(aa_line, g_line, label='g')
plt.ylim(-0.1,1)
print(y,g,y_all,g_all)
plt.show()