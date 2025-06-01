import numpy as np
import matplotlib.pyplot as plt

delta = 0.015
x = np.arange(0, 2, delta)
h = lambda t: 10.138* np.exp(-13.45*t) * np.sin(15.78*t)
h1 = lambda t: 0.37 - 0.37 * np.exp(-13.45*t) * np.cos(15.78*t) - 0.32 * np.exp(-13.45*t) * np.sin(15.78*t)
i_0 = lambda t: 2*np.sin( 2.5 *np.pi * t ) +2 * np.sin( 2.5 * np.pi * (t-0.4) ) * list(map(lambda x: 0 if x<0.4 else 1, t))
def i_t(t):
    if t < 0.4:
        return (-0.375*np.cos( 7.85*t ) + 0.65*np.sin( 7.85*t) + 0.37 * np.exp(-13.45*t)*np.cos( 15.78*t ) - 0.0057*np.exp(-13.45*t)*np.sin( 15.78*t ))
    else:
        return (-0.375*np.cos( 7.85*t ) + 0.65*np.sin( 7.85*t) + 0.37 * np.exp(-13.45*t)*np.cos( 15.78*t ) - 0.0057*np.exp(-13.45*t)*np.sin( 15.78*t )) + \
    (-0.375*np.cos( 7.85*(t-0.4) ) + 0.65*np.sin( 7.85*(t-0.4) ) + 0.37 * np.exp(-13.45*(t-0.4))*np.cos( 15.78*(t-0.4) ) - 0.0057*np.exp(-13.45*(t-0.4))*np.sin( 15.78*(t-0.4) ))
    
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.grid('on')
ax2.grid('on')
ax1.set_xticks(np.arange(0, 2, 0.1), minor=True)
ax1.set_yticks(np.arange(0, 3.5, 0.1), minor=True)
ax2.set_xticks(np.arange(0, 2, 0.1), minor=True)
ax2.set_yticks(np.arange(0, 3.5, 0.1), minor=True)
ax1.plot(x, h(x), label="h(t)")
ax1.plot(x, h1(x), label="h1(t)")
ax2.plot(x, i_0(x), label="i0(t)")
ax2.plot(x, [i_t(i) for i in x], label="i(t)")
ax1.legend()
ax2.legend()
plt.show()