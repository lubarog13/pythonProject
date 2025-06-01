import numpy as np
import matplotlib.pyplot as plt

def i_t(t):
    if t < 0.4:
        return (-0.375*np.cos( 7.85*t ) + 0.65*np.sin( 7.85*t) + 0.37 * np.exp(-13.45*t)*np.cos( 15.78*t ) - 0.0057*np.exp(-13.45*t)*np.sin( 15.78*t ))
    else:
        return (-0.375*np.cos( 7.85*t ) + 0.65*np.sin( 7.85*t) + 0.37 * np.exp(-13.45*t)*np.cos( 15.78*t ) - 0.0057*np.exp(-13.45*t)*np.sin( 15.78*t )) + \
    (-0.375*np.cos( 7.85*(t-0.4) ) + 0.65*np.sin( 7.85*(t-0.4) ) + 0.37 * np.exp(-13.45*(t-0.4))*np.cos( 15.78*(t-0.4) ) - 0.0057*np.exp(-13.45*(t-0.4))*np.sin( 15.78*(t-0.4) ))
    
def furier_I(x):
    if (x <0):
        return 0
    return 0.474 / 2  + 0.377*np.cos(2.5*np.pi*x-2.09) + 0.147 *np.cos(5*np.pi*x - 4.303)

def approx_I(x):
    if (x < 0 or x > 0.4):
        return 0
    elif (x<0.116):
        return i_t(x)
    elif (x > 0.4):
        return i_t(x)
    else:
        return furier_I(x)

x = np.arange(0, 3, 0.01)
y = [furier_I(i) for i in x]
y_0 = [i_t(i) for i in x]
y_approx = [approx_I(i) for i in x]

plt.plot(x, y, label='Фурье')
plt.plot(x, y_0, label='i(н)', linestyle='--')
# plt.plot(x, y_approx, label='Аппроксимация рядом Фурье')
plt.legend()
plt.show()