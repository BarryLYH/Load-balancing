import matplotlib.pyplot as plt

x = 0.001
x_line = []
y_line = []
r=10
d=2
l = 0.8

while x < 1:
    k = 0
    for i in range(1, 50):
        upper = (r ** i) * (1 - l * (x**d)) ** i
        lower = 1
        for j in range(1, i + 1):
            lower = lower * (r * (1 - x**d) / (1 - x) + j * (x**d))
        k = k + upper / lower * x
    result = k + x
    x_line.append(x)
    y_line.append(result)
    x += 0.001

plt.plot(x_line,y_line)
plt.show()