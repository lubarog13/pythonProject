import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from main import *
import random
from BBsearch import *


def contourPlot(ax, f):
    # Подготовка к рисованию, настраиваем оси x и y
    x1 = np.arange(-4, 4.1, 0.1)
    m = len(x1)
    y1 = np.arange(-4, 4.1, 0.1)
    n = len(y1)

    # делаем сетку
    [xx, yy] = np.meshgrid(x1, y1)

    # массивы для графиков функции и ее производных по x и y
    F = np.zeros((n, m))

    # вычисляем рельеф поверхности
    for i in range(n):
        for j in range(m):
            X = [xx[i, j], yy[i, j]]
            F[i, j] = f(X)

    nlevels = 20
    ax.contour(xx, yy, F, nlevels, linewidths=1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')


#   - если не задавать цвет, то на итоговом графике видны шаги и маркер выглядит тогда лишним
# из минуса - нет возможности приближать график
def bbdDraw(ax, coords, nsteps):
    fSize = 11
    x0 = coords[0]
    ax.text(x0[0] + 0.1, x0[1] + 0.1, str(0), fontsize=fSize)
    for i in range(nsteps - 1):
        x0 = coords[i]
        x1 = coords[i + 1]
        ax.plot([x0[0], x1[0]], [x0[1], x1[1]], lw=1.2, marker='s', ms=3)

    ax.text(x1[0] + 0.2, x1[1], str(nsteps), fontsize=fSize)
    plt.scatter(x1[0], x1[1], marker='o', c='red', zorder=12)


def draw(coords, nsteps, f):
    fig, ax = plt.subplots()
    fig.suptitle('Barzilai-Borwein 1 method each step visualisation & Countour plot')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.gca().set_aspect('equal', adjustable='box')
    bbdDraw(ax, coords, nsteps)
    contourPlot(ax, f)
    name = "plot.png"
    fig.savefig(name)
    ad = "<img width=\"900px\" src=\"/resources/" + name + "\">"
    print(ad)

def main():
    print("Rosenbrock function:")
    x0 = np.array([[2], [-1]])
    tol = 1e-9
    [xmin, f, neval, coords] = bbsearch(fR, dfR, x0, tol)  # r - функция Розенброка
    print(xmin, f, neval)
    draw(coords,  len(coords), fR)
    #contourPlot()
    #bbdDraw(coords, neval)
    # Уточнить разницу в результатах - matlab - xmin 1.00000
    #                                                1.00000
    #                                           fmin 2.8911e-20
    #                                           neval 90
    # и Питон- [[1.]
    #           [1.]] [2.93450702e-20] 90
    # вероятно связано с разницей хранения знаков и округлении
    # В таком случае тесты делать на xmin или fmin?

if __name__ == '__main__':
    main()




