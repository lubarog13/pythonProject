import numpy as np
import sys
from numpy.linalg import norm

np.seterr(all='warn')


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


def H(X, tol, df):
    # PLACE YOUR CODE HERE
    x0 = X[0]
    y0 = X[1]
    dfx = lambda x: df(x)[0]
    dfy = lambda y: df(y)[1]
    deltaX = tol * 0.1
    dx = ((dfx([x0 + deltaX, y0]) - dfx([x0 - deltaX, y0])) / (2 * deltaX))[0]
    dy = ((dfy([x0, y0 + deltaX]) - dfy([x0, y0 - deltaX])) / (2 * deltaX))[0]
    dxy = ((dfx([x0, y0 + deltaX]) - dfx([x0, y0 - deltaX])) / (2 * deltaX))[0]
    ddf = np.array(([dx, dxy], [dxy, dy]))
    return ddf


def nsearch(f, df, x0, tol):
    # NSEARCH searches for minimum using Newton method
    # 	answer_ = nsearch(f, df, x0, tol)
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

    neval = 1
    x = x0
    coords = [x]
    kmax = 1000
    deltaX = tol + 1
    while (norm(deltaX) >= tol) and (neval < kmax):
        g0 = df(x)
        deltaX = np.linalg.solve(H(x, tol, df), g0)
        x = x - deltaX
        neval = neval + 1
        coords.append(x)
    answer_ = [x, f(x), neval, coords]
    return answer_