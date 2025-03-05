
import numpy as np


def f(x): return (x - 3) ** 2 - 3 * x + x ** 2 - 40


def gsearch(interval, tol):
    # GOLDENSECTIONSEARCH searches for minimum using golden section
    # 	[xmin, fmin, neval] = GOLDENSECTIONSEARCH(f,interval,tol)
    #   INPUT ARGUMENTS
    # 	f is a function
    # 	interval = [a, b] - search interval
    # 	tol - set for bot range and function value
    #   OUTPUT ARGUMENTS
    # 	xmin is a function minimizer
    # 	fmin = f(xmin)
    # 	neval - number of function evaluations
    #   coords - array of statistics,  coord[i][:] =  [x1,x2, a, b]

    # PLACE YOUR CODE HERE
    xmin = 0
    neval = 1
    a = interval[0]
    b = interval[1]
    l = np.abs(b - a)
    fib = (1 + np.sqrt(5)) / 2
    x1 = b - l / fib
    x2 = a + l / fib
    y1 = f(x1)
    y2 = f(x2)
    coord = []
    coord.append([x1, x2, a, b])
    while (np.abs(l) > tol):
        if y1 > y2:
            a = x1
            xmin = x2
            y1 = y2
            x1 = x2
            l = np.abs(b - a)
            x2 = a + l / fib
            y2 = f(x2)
        else:
            b = x2
            xmin = x1
            x2 = x1
            y2 = y1
            l = np.abs(b - a)
            x1 = b - l / fib
            y1 = f(x1)
        neval=neval+1
        coord.append([x1, x2, a, b])
    answer_ = [xmin, f(xmin), neval, coord]
    return answer_