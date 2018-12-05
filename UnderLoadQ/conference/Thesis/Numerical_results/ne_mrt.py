r= 100
d = 4
lam = [0.80, 0.81,0.82, 0.83, 0.84, 0.85, 0.86,0.87,0.88,0.89,0.90,0.91,0.92,0.93,0.94
       ,0.95, 0.96, 0.97, 0.98, 0.99]
ne_p0 = []
for l in lam:
    p0 = 0
    while p0 < 1:
        p0 += 0.0001
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
 #   print(p0)
    ne_p0.append(p0)
print('ne',ne_p0)


ne_mrt = []
for i in range(len(lam)):
    m = 1 / (1 - (ne_p0[i] ** d) * lam[i])
    ne_mrt.append(m)

print('NE   r={}   d={}    mrt={}'.format(r, d, ne_mrt))
