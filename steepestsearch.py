import numpy as np
import sys
from numpy.linalg import norm


def goldensectionsearch(f, interval, tol):
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
        neval = neval + 1
        coord.append([x1, x2, a, b])
    answer_ = [xmin, f(xmin), neval]
    return answer_


# F_HIMMELBLAU is a Himmelblau function
# 	v = F_HIMMELBLAU(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a function value
def fH(X):
    x = X[0]
    y = X[1]
    v = (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2
    return v


# DF_HIMMELBLAU is a Himmelblau function derivative
# 	v = DF_HIMMELBLAU(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a derivative function value

def dfH(X):
    x = X[0]
    y = X[1]
    v = np.copy(X)
    v[0] = 2 * (x ** 2 + y - 11) * (2 * x) + 2 * (x + y ** 2 - 7)
    v[1] = 2 * (x ** 2 + y - 11) + 2 * (x + y ** 2 - 7) * (2 * y)

    return v


# F_ROSENBROCK is a Rosenbrock function
# 	v = F_ROSENBROCK(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a function value

def fR(X):
    x = X[0]
    y = X[1]
    v = (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    return v


# DF_ROSENBROCK is a Rosenbrock function derivative
# 	v = DF_ROSENBROCK(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a derivative function value

def dfR(X):
    x = X[0]
    y = X[1]
    v = np.copy(X)
    v[0] = -2 * (1 - x) + 200 * (y - x ** 2) * (- 2 * x)
    v[1] = 200 * (y - x ** 2)
    return v


def sdsearch(f, df, x0, tol):
    # SDSEARCH searches for minimum using steepest descent method
    # 	answer_ = sdsearch(f, df, x0, tol)
    #   INPUT ARGUMENTS
    #   f  - objective function
    #   df - gradient
    # 	x0 - start point
    # 	tol - set for bot range and function value
    #   OUTPUT ARGUMENTS
    #   answer_ = [xmin, fmin, neval, coords]
    # 	xmin is a function minimizer
    # 	fmin = f(xmin)
    # 	neval - number of function evaluations
    #   coords - array of statistics

    # PLACE YOUR CODE HERE
    neval = 0
    kmax = 1000
    coords = []
    x = x0
    deltaX = tol + 0.01
    while (norm(deltaX) >= tol) and (neval < kmax):
        al = goldensectionsearch(lambda a: f(x - a*df(x)), [0, 1], tol)[0]
        deltaX = al * df(x)
        x = x - deltaX
        neval += 1
        coords.append(x)
    answer_ = [x, f(x), neval, coords]
    return answer_