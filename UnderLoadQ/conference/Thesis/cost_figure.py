import matplotlib.pyplot as plt
lam = [0.5, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99]

r = 20
d = 2

pod = [13230509.0, 13562669.0, 13934061.0, 14419569.0, 15035601.0, 15892441.0, 17065213.0, 18854945.0, 21923973.0, 28133025.0, 30421461.0, 33236633.0, 36824569.0, 41400769.0]
ne = [11934734.0, 12018839.0, 12104186.0, 12238332.0, 12398816.0, 12621369.0, 12984766.0, 13618393.0, 15050523.0, 18962062.0, 20511537.0, 22852005.0, 26125596.0, 31228168.0]
e = [47936235.0, 47718531.0, 47449138.0, 47070672.0, 46584840.0, 45933690.0, 44939217.0, 43260824.0, 39949645.0, 30744874.0, 27152066.0, 22038383.0, 17234233.0, 13806567.0]

plt.xlabel('Load')
plt.ylabel('Communication Cost')
plt.plot(lam, pod, 'r-', label='JIQ-Pod')
plt.plot(lam, ne, 'b--', label='JIQ-NE')
plt.plot(lam, e, 'k-.', label='JIQ-E')
plt.legend(loc='upper left')
plt.xlim(0.8, 0.99)
plt.show()