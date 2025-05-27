import numpy as np
import matplotlib.pyplot as plt

def i_t(t):
    if t < 0 or t > 0.4:
        return 0
    else:
        return (-0.375*np.cos( 7.85*t ) + 0.65*np.sin( 7.85*t) + 0.37 * np.exp(-13.45*t)*np.cos( 15.78*t ) - 0.0057*np.exp(-13.45*t)*np.sin( 15.78*t ))
    
def furier_I(x):
    if (x <0):
        return 0
    return 0.75 / 2  + 0.039*np.cos(7.5*np.pi*x-0.19) + 0.0055*np.cos(12.5*np.pi*x-7.049)

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

plt.plot(x, y, label='Фурье', linestyle='--')
plt.plot(x, y_0, label='i(н)', linestyle='--')
plt.plot(x, y_approx, label='Аппроксимация рядом Фурье')
plt.legend()
plt.show()