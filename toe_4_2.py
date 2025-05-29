import numpy as np
import matplotlib.pyplot as plt

a = [1.27,1, 0.424, 0, 0.085, 0, 0.036, 0 ]
fx = [0, -np.pi/2, -np.pi /2, -np.pi, 0, -np.pi/2, -np.pi /2, -np.pi]
x = [0, 1, 2, 3, 4, 5, 6, 7]

f, (ax1) = plt.subplots(1, 1)
for i in range(len(a)):
    ax1.vlines(x=x[i], ymin=fx[i], ymax=0, linewidth=2, color='violet')
ax1.set_xticks(x, labels=["0", "2.5π", "5π", "7.5π", "10π", "12.5π", "15π", "17.5π"])
ax1.grid('on')
ax1.legend()
plt.show()