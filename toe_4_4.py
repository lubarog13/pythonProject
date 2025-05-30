import numpy as np
import matplotlib.pyplot as plt

def I_0(x):
    if x < 0 or x > 0.4:
        return 0
    else:
        return 2*np.sin(2.5*np.pi*x)
    
def furier_I(x):
    if (x <0):
        return 0
    return 0.635 + np.cos(2.5*np.pi*x-0.5*np.pi) + 0.042*np.cos(5*np.pi*x)

def approx_I(x):
    if (x < 0 or x > 0.4):
        return 0
    elif (x<0.067):
        return I_0(x)
    elif (x > 0.31):
        return I_0(x)
    else:
        return furier_I(x)

x = np.arange(0, 3, 0.01)
y = [furier_I(i) for i in x]
y_0 = [I_0(i) for i in x]
y_approx = [approx_I(i) for i in x]

plt.plot(x, y, label='Фурье')
plt.plot(x, y_0, label='i(0)', linestyle='--')
# plt.plot(x, y_approx, label='Аппроксимация рядом Фурье')
plt.legend()
plt.show()