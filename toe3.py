import numpy as np
import matplotlib.pyplot as plt

delta = 0.015
x = np.arange(0.1, 3, delta)
h = lambda t: 11.27* np.exp(-7.7*t) * np.sin(14.32*t)
h1 = lambda t: 0.61 - 0.61 * np.exp(-7.7*t) * np.cos(14.32*t) - 0.33 * np.exp(-7.7*t) * np.sin(14.32*t)
i_0 = lambda t: 2*np.sin( 2.5 *np.pi * t ) +2 * np.sin( 2.5 * np.pi * (t-0.4) ) * list(map(lambda x: 0 if x<0.4 else 1, t))
i_t = lambda t: (-0.69*np.cos( -7.85*t ) + 1.16*np.sin(7.85*t) + 0.69 * np.exp(-7.7*t)*np.cos( 14.32*t ) - 0.26*np.exp(-7.7*t)*np.sin( 14.32*t ))* list(map(lambda x: 1 if x<0.4 else 0, t))
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, h(x), label="h(t)")
ax1.plot(x, h1(x), label="h1(t)")
ax2.plot(x, i_0(x), label="i0(t)")
ax2.plot(x, i_t(x), label="i(t)")
ax1.legend()
ax2.legend()
plt.show()