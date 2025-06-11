import numpy as np

def euler(func, x_0, y_0, delta, n):
    """
        Метод Эйлера
        Входные данные:
            func - нужная функцияя
            x_0, y_0 - начальное значение
            delta - шаг
            n - количество итераций
        Возвращаемые значения:
            (x,y) - решение
            path -
    """
    x, y = x_0, y_0
    path = [(x_0, y_0)]
    for i in range(n):
        y += delta * func(x,y)
        x += delta
        path.append((x, y))
    return (x,y), path


from matplotlib import pyplot as plt

funcU = lambda u, i: -14.4*u + 20 * i - 115.2
funcI = lambda u, i: -12.5*u - 12.5 * i + 37.5
u0, i0 = 54/43, 75/43
delta = 0.015
b = 1.5


def twoFunctionsEuler(func1, func2, x_0, y_0, delta, max):
    x, y = x_0, y_0
    t = 0
    path1 = [(t, x_0)]
    path2 = [(t, y_0)]
    n = round((max - t) / delta)
    for i in range(n):
        x_prev = x
        x += delta * func1(x,y)
        print(x, x_prev)
        y += delta * func2(x_prev,y)
        t += delta
        path1.append((t, x))
        path2.append((t, y))
    print(path1)
    return path1, path2

def plot_euler(euler_method, func, x_0, y_0, n, delta, label):
    res, path = euler_method(func, x_0, y_0, n=n, delta=delta)
    path = np.array(path)
    plt.plot(path[:, 0], path[:, 1], color='r', alpha=plot_euler.alpha,
             label=label)
    plot_euler.alpha += 0.1

def plot_two_functions_euler(func1, func2, x_0, y_0, max, delta, labels, index):
    path1, path2 = twoFunctionsEuler(func1, func2, x_0, y_0, max=max, delta=delta)
    path1 = np.array(path1)
    path2 = np.array(path2)
    if index=='x':
        plt.plot(path1[:, 0], path1[:, 1], color='r',
             label=labels[0], linestyle='--')
    else:
        plt.plot(path2[:, 0], path2[:, 1], color='b',
             label=labels[1], linestyle='--')


def plot_good(func, x_0, y_0, b):
    n = 1000
    delta = (b - x_0) / n
    path = np.array(euler(func, x_0, y_0, n=n, delta=delta)[1])
    plt.plot(path[:, 0], path[:, 1], color='y', label=f'Actual')


def iterate_plot(euler_method, func, x_0, y_0, b):
    plt.figure(facecolor='0.1', figsize=(10, 6))
    plot_euler.alpha = 0.2
    for n in np.linspace(2, 30, 8, dtype=int):
        delta = (b - x_0) / n
        plot_euler(euler_method, func, x_0, y_0, delta=delta, n=n)
    plot_good(func, x_0, y_0, b)
    plt.legend()
    plt.title(euler_method.__name__)

# plt.figure(facecolor='0.1', figsize=(10, 6))
# plot_euler.alpha = 0.2
# plot_euler(euler, funcU, u0, i0, 10, delta, 'U')
# # plot_good(funcU, u0, i0, 10)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, delta*200, delta)
#plt.plot(x, -144/43*np.exp(-13.45*x)*np.cos(0.15*np.sqrt(11071)*x) -32280/11309 *np.exp(-13.45*x)*np.sin(0.15*np.sqrt(11071)*x) + 198/43, label="iL", color='r')
plt.plot(x, 144/43*np.exp(-13.45*x)*np.cos(0.15*np.sqrt(11071)*x) -50280/11309 *np.exp(-13.45*x)*np.sin(0.15*np.sqrt(11071)*x) - 69/43, label="Uc")
plot_two_functions_euler(funcU, funcI, u0, i0, delta*200, delta, ['Uc(эйлер)', 'iL(эйлер)'], 'x')
plt.legend()
plt.show()