import math

import numpy as np
import matplotlib.pyplot as plt

a = lambda x:  np.abs(31.42/(61.69-np.pow(x,2)) * np.sin(0.2*x))

x = np.arange(0, 6 * math.pi / 0.4, math.pi/0.4)
plt.plot(x, a(x), label="A")
plt.show()