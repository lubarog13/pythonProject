import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 0.024*10, 0.024)
t_x = np.arange(0, 0.024*10, 0.024)
t_y = [-3.9,-7.53,
-8.25,
-7.03,
-4.96,
-2.88,
-1.31,
-0.44,
-0.20,
-0.41,
]
plt.plot(x, -2.3 * np.exp(-13.45*x) * np.cos(15.78*x) -11.53 * np.exp(-13.45*x) * np.sin(15.78*x) - 1.6, t_x, t_y)
plt.plot()
plt.show()
