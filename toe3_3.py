import math

import numpy as np
import matplotlib.pyplot as plt

a = lambda x:  np.abs(10*np.pi/((6.25*np.pow(np.pi, 2))-np.pow(x,2)) * np.cos(0.2*x))

x = np.arange(0, 6 * math.pi / 0.4, 0.1)
f, (ax1) = plt.subplots(1, 1)
ax1.plot(x, a(x), label="A")
# print(0.1 * a(0))
ax1.hlines(y=0.1 * a(0), xmin=0, xmax=6 * math.pi / 0.4, linewidth=1, color='y')
ax1.plot(20.5, 0.05, '.', color="blue")
ax1.hlines(y=0, xmin=0, xmax=20.5, linewidth=1, color='blue')
ax1.vlines(x=20.5, ymin=0, ymax=0.05, linewidth=1, color='blue')
ax1.text(0.2, 0.05, "Δw", transform=ax1.transAxes, fontsize=12,
        verticalalignment='top')
ax1.set_xticks(np.arange(0, 6 * math.pi / 0.4, math.pi / 0.4), labels=["0", "2.5π", "5π", "7.5π", "10π", "12.5π"])
ax1.grid('on')
ax1.legend()
plt.show()