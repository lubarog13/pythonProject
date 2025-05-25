import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
def argand(a):
    for x in range(len(a)):
        plt.plot([0,a[x].real],[0,a[x].imag],'ro-',label='H(jw)')
    limit=np.max(np.ceil(np.absolute(a))) # set limits for axis
    plt.xlim((-limit,limit))
    plt.ylim((-limit,limit))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.vlines(x=0, ymin=-limit, ymax=limit, linewidth=1, color='black', alpha=0.7)
    plt.hlines(y=0, xmin=-limit, xmax=limit, linewidth=1, color='black', alpha=0.7)
    plt.show()
delta = 0.01
x = np.arange(0,1000, 1)
hI = lambda w: 160 / ( (430 - np.pow(w, 2)) + 26.9j*w )
hI_mod = lambda w: 160 / (np.sqrt(np.pow(w,4) - 291.64*np.pow(w,2) + 264.4*264.4 ))
f_w = lambda w: -1*np.atan( 15.4*w/(264.4-np.pow(w,2)) )
# h1 = lambda t: 0.61 - 0.61 * np.exp(-7.7*t) * np.cos(14.32*t) - 0.33 * np.exp(-7.7*t) * np.sin(14.32*t)
# i_0 = lambda t: 2*np.sin( 2.5 *np.pi * t ) +2 * np.sin( 2.5 * np.pi * (t-0.4) ) * list(map(lambda x: 0 if x<0.4 else 1, t))
# i_t = lambda t: (-0.69*np.cos( -7.85*t ) + 1.16*np.sin(7.85*t) + 0.69 * np.exp(-7.7*t)*np.cos( 14.32*t ) - 0.26*np.exp(-7.7*t)*np.sin( 14.32*t ))* list(map(lambda x: 1 if x<0.4 else 0, t))
# f, (ax1) = plt.subplots(1, 1)
# for x in range(len(a)):
# ax1.plot([0,hI(x).real],[0,hI(x).real], label="H(jw)")
# ax1.plot(x, hI_mod(x), '-', label="|H(jw)|")
# ax1.plot(0.707, hI_mod(0.707), '.', color="blue")
# ax1.vlines(x=0.707, ymin=0, ymax=1, linewidth=1, color='y', alpha=0.7)
# ax1.set_yticks(np.arange(0, 250, 5), minor=True)
# ax1.set_xticks(np.arange(0, 1, 0.05), minor=True)
# print(hI_mod(0.707))
# ax1.grid('on')
# ax1.tick_params(axis='x', color='m', length=4, direction='in', width=4,
#                        labelcolor='g', grid_color='b')
# plt.plot(x, f_w(x), label="Ф(w)")
# ax1.plot(x, hI_mod(x), label="|H(jw)|")
# ax1.plot(x, h1(x), label="h1(t)")
# ax2.plot(x, i_0(x), label="i0(t)")
# ax2.plot(x, i_t(x), label="i(t)")
# ax1.legend()
# plt.legend()
# plt.show()
a = hI(x)
argand(a)