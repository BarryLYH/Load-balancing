r= 100
d = 4
lam = [0.80, 0.81,0.82, 0.83, 0.84, 0.85, 0.86,0.87,0.88,0.89,0.90,0.91,0.92,0.93,0.94
       ,0.95, 0.96, 0.97, 0.98, 0.99]
def metime(d, l, p):
    k = 0
    for i in range(1,50):
        # h1 = ((d**i) - 1)/(d-1)
        # h2 = ((d**(i-1))-1)/(d-1)
        s = l**((d**i-1)/(d-1)) * p**((d**(i-1)-1)/(d-1))
        k = k + (s**d)
    return(1+p*k)



pod_p0 = []
for l in lam:
    p0 = 0
    while p0 < 1:
        p0 += 0.0001
        k = 0
        for i in range(1, 40):
            upper = (r**i) *( (1 - (l**d) * p0)**i )
            lower = 1
            for j in range(1, i+1):
                lower = lower * (r + j*p0*( (1-l**d)/(1-l) ))
            k = k + upper / lower * p0
        result = k + p0
        if abs(result - 1) < 0.001:
            break
    pod_p0.append(p0)
print('pod', pod_p0)


pod_mrt = []
for i in range(len(lam)):
    pod_mrt.append(metime(d, lam[i], pod_p0[i]))



print('Pod   r={}   d={}    mrt={}'.format(r, d, pod_mrt))
