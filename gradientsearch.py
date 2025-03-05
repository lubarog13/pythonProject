import numpy as np
import sys
from numpy.linalg import norm


# F_HIMMELBLAU is a Himmelblau function
# 	v = F_HIMMELBLAU(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a function value
def f(X):
    x = X[0]
    y = X[1]
    # Версия питона в codeboard не поддерживает метод библиотеки numpy float_power
    v = (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2
    return v


# DF_HIMMELBLAU is a Himmelblau function derivative
# 	v = DF_HIMMELBLAU(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a derivative function value
def df(X):
    x = X[0]
    y = X[1]
    v = np.copy(X)
    v[0] = 2 * (x ** 2 + y - 11) * (2 * x) + 2 * (x + y ** 2 - 7)
    v[1] = 2 * (x ** 2 + y - 11) + 2 * (x + y ** 2 - 7) * (2 * y)
    return v


def grsearch(x0, tol):
    # GRSEARCH searches for minimum using gradient descent method
    # 	answer_ = grsearch(x0,tol)
    #   INPUT ARGUMENTS
    #	x0 - starting point
    # 	tol - set for bot range and function value
    #   OUTPUT ARGUMENTS
    #   answer_ = [xmin, fmin, neval, coords]
    # 	xmin is a function minimizer
    # 	fmin = f(xmin)
    # 	neval - number of function evaluations
    #   coords - array of x values found during optimization

    # PLACE YOUR CODE HERE
    neval = 1
    kmax = 1000
    coords = [x0]
    x = x0
    al = 0.01
    deltaX = x + tol*2
    while (norm(deltaX) >= tol) and (neval < kmax):
        g = -1*df(x)
        x = x + al*g
        deltaX = abs(al*g)
        neval+=1
        coords.append(x)
    answer_ = [x, f(x), neval, coords]
    return answer_