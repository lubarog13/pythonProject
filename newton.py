import numpy as np

def f(x): return x**2 - 10*np.cos(0.3*np.pi*x) - 20
def df(x): return 2*x + 3*np.pi*np.sin(0.3*np.pi*x)
def ddf(x): return 2 + 0.9*(np.pi**2)*np.cos(0.3*np.pi*x)

def nsearch(tol, x0):
# NSEARCH searches for minimum using Newton method
# 	answer_ = nsearch(tol,x0)
#   INPUT ARGUMENTS
# 	tol - set for bot range and function value
#	x0 - starting point
#   OUTPUT ARGUMENTS
#   answer_ = [xmin, fmin, neval, coords]
# 	xmin is a function minimizer
# 	fmin = f(xmin)
# 	neval - number of function evaluations
#   coords - array of x values found during optimization

	#PLACE YOUR CODE HERE
    neval = 1
    x = x0
    x1 = x0 + 2*tol
    coords = [x]
    while (np.abs(x1 - x)) >= tol:
        x = x1
        x1 = x - df(x)/ddf(x)
        neval = neval+1
        coords.append(x1)
    answer_ = [x1, f(x1), neval, coords]
    return answer_