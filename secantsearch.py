import numpy as np

def f(x): return x**2 -  10*np.cos(0.3*np.pi*x) - 20
def df(x): return 2*x + 3*np.pi*np.sin(0.3*np.pi*x)

def ssearch(interval,tol):
    # SSEARCH searches for minimum using secant method
    # 	answer_ = ssearch(interval,tol)
    #   INPUT ARGUMENTS
    # 	interval = [a, b] - search interval
    # 	tol - set for bot range and function value
    #   OUTPUT ARGUMENTS
    #   answer_ = [xmin, fmin, neval, coords]
    # 	xmin is a function minimizer
    # 	fmin = f(xmin)
    # 	neval - number of function evaluations
    #   coords - array of x values found during optimization

    # PLACE YOUR CODE HERE
    a = interval[0]
    b = interval[1]
    neval = 1
    x = b - df(b)*(b - a)/(f(b) - f(a))
    coords = [[x,a,b]]
    while (np.abs(df(x))) > tol and (np.abs(b - a)) > tol:
        if df(x) >0:
            b = x
        else:
            a = x
        x = b - df(b) * (b - a) / (df(b) - df(a))
        coords.append([x,a,b])
        neval+=1
    answer_ = [x, f(x), neval, coords]
    return answer_