import numpy as np
import sys
from numpy.linalg import norm
from numpy.linalg import inv
np.seterr(divide='ignore', invalid='ignore')


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


def nagsearch(f, df, x0, tol):
    
# NAGSEARCH searches for minimum using the Nesterov accelerated gradient method
# 	answer_ = nagsearch(f, df, x0, tol)
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

    #PLACE YOUR CODE HERE
    neval = 1
    x = x0
    coordinates = [x]
    al = 0.05
    eta = al / 10 
    gamma = 0.75
    kmax = 1000
    y=x0
    while (norm(df(x)) >= tol) and (neval < kmax):
        x_1 = y - eta*df(y)
        y = x + gamma * (x_1 - x)
        x = x_1
        coordinates.append(x)
        neval+=1


    answer_ = [x, f(x), neval, coordinates]
    return answer_
