import matplotlib.pyplot as plt

lam = [0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
JIQ_Pod = [0.12354, 0.15468, 0.20381, 0.28988, 0.46912, 0.64921, 0.90279]
JIQ_NE =[0.15661, 0.18871, 0.23730, 0.31910, 0.48458, 0.65075, 0.89048]
JIQ_E = [0.08112, 0.10285, 0.13814, 0.20446, 0.36812, 0.57296, 0.88916]
JIQ = [0.13212, 0.16533, 0.21631, 0.30308, 0.47861, 0.65271, 0.89919]

plt.xlabel('Load')
plt.ylabel('Idle Iqueue Rate')

plt.plot(lam, JIQ_NE, 'bs--', label='JIQ-NE')
plt.plot(lam, JIQ_Pod, 'rx-', label='JIQ-Pod')
plt.plot(lam, JIQ_E, 'kD:', label='JIQ-E')
plt.plot(lam, JIQ, 'gx:', label='JIQ')

plt.legend()
plt.xlim(0.50, 0.99)
plt.show()
