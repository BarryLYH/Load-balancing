r= 100
d = 4
lam = [0.5, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99]
'''
p1 = []
for l in lam:
    p0 = 0
    while p0 < 1:
        p0 += 0.00001
        k = 0
        for i in range(1, 50):
            upper = (r**i) *( (1 - (l**d) * p0)**i )
            lower = 1
            for j in range(1, i+1):
                lower = lower * (r + j*p0*( (1-l**d)/(1-l) ))
            k = k + upper / lower * p0
        result = k + p0
        if abs(result - 1) < 0.001:
            break
    print(p1)
    p1.append(p0)
print('pod',p1)
'''
'''
p2 = []
for l in lam:
    p0 = 0
    while p0 < 1:
        p0 += 0.00001
        k = 0
        for i in range(1, 50):
            upper = (r**i) * (1 - l * (p0**d))**i
            lower = 1
            for j in range(1, i+1):
                lower = lower * (r * (1- p0**d) / (1-p0) + j*(p0**d))
            k = k + upper / lower * p0
        result = k + p0
        if abs(result - 1) < 0.001:
            break
    print(p2)
    p2.append(p0)
print('ne',p2)
'''

p3 = []
for l in lam:
    p0 = 0
    while p0 < 1:
        p0 += 0.00001
        k = 0
        for i in range(1, 50):
            o = (d-1) * (i-1)
            upper = (r**i) * ((1 - (l * p0))**i) * ((1-p0)**o)
            lower = 1
            for j in range(1, i+1):
                lower = lower * (r + j*p0 )
            k = k + upper / lower * (1-(1-p0)**d)
        result = k + p0

        if abs(result - 1) < 0.001:
            break
    print(p0)
    p3.append(p0)
print('e',p3)

'''
p4 = []
for l in lam:
    p0 = 0
    while p0 < 1:
        p0 += 0.00001
        k = 0
        for i in range(1, 50):
            upper = (r**i) * ((1 - (l * p0))**i)
            lower = 1
            for j in range(1, i+1):
                lower = lower * (r + j*p0 )
            k = k + upper / lower * p0
        result = k + p0

        if abs(result - 1) < 0.0001:
            break
    print(p0)
    p4.append(p0)
print('jiq', p4)
'''