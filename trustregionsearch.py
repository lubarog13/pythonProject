import numpy as np
import sys
from numpy.linalg import norm
from numpy.linalg import inv


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


def goldensectionsearch(f, interval, tol):
    a = interval[0]
    b = interval[1]
    Phi = (1 + np.sqrt(5)) / 2
    L = b - a
    x1 = b - L / Phi
    x2 = a + L / Phi
    y1 = f(x1)
    y2 = f(x2)
    neval = 2
    xmin = x1
    fmin = y1

    # main loop
    while np.abs(L) > tol:
        if y1 > y2:
            a = x1
            xmin = x2
            fmin = y2
            x1 = x2
            y1 = y2
            L = b - a
            x2 = a + L / Phi
            y2 = f(x2)
            neval += 1
        else:
            b = x2
            xmin = x1
            fmin = y1
            x2 = x1
            y2 = y1
            L = b - a
            x1 = b - L / Phi
            y1 = f(x1)
            neval += 1

    answer_ = [xmin, fmin, neval]
    return answer_


def pparam(pU, pB, tau):
    if (tau <= 1):
        p = np.dot(tau, pU)
    else:
        p = pU + (tau - 1) * (pB - pU)
    return p


def doglegsearch(mod, g0, B0, Delta, tol):
    # dogleg local search
    xcv = np.dot(-g0.transpose(), g0) / np.dot(np.dot(g0.transpose(), B0), g0)
    pU = xcv * g0
    xcvb = inv(- B0)
    pB = np.dot(inv(- B0), g0)

    func = lambda x: mod(np.dot(x, pB))
    al = goldensectionsearch(func, [-Delta / norm(pB), Delta / norm(pB)], tol)[0]
    pB = al * pB
    func_pau = lambda x: mod(pparam(pU, pB, x))
    tau = goldensectionsearch(func_pau, [0, 2], tol)[0]
    pmin = pparam(pU, pB, tau)
    if norm(pmin) > Delta:
        pmin_dop = (Delta / norm(pmin))
        pmin = np.dot(pmin_dop, pmin)
    return pmin


def trustreg(f, df, x0, tol):
    # TRUSTREG searches for minimum using trust region method
    # 	answer_ = trustreg(f, df, x0, tol)
    #   INPUT ARGUMENTS
    #   f  - objective function
    #   df - gradient
    # 	x0 - start point
    # 	tol - set for bot range and function value
    #   OUTPUT ARGUMENTS
    #   answer_ = [xmin, fmin, neval, coords, radii]
    # 	xmin is a function minimizer
    # 	fmin = f(xmin)
    # 	neval - number of function evaluations
    #   coords - array of statistics
    #   radii - array of trust regions radii

    # PLACE YOUR CODE HERE
    neval = 1
    x = x0
    kmax = 1000
    coords = [x]
    g0 = df(x)
    p = -g0
    dx = tol + 0.1
    eta = 0.1
    radii = [eta]
    h = np.eye(2)
    delta = eta
    f_1 = f(x)

    while (norm(dx) >= tol) and (neval < kmax):
        m = lambda p0: f(x) + np.dot(p0.transpose(), g0) + 0.5 * np.dot(np.dot(p0.transpose(), h), p0)
        p = doglegsearch(m, g0, h, delta, tol)
        rad = (f_1 - f(x + p)) / (m(np.zeros((2, 1))) - m(p))
        f_1 = f(x+p)
        if (np.abs(rad) > eta):
            x_1 = x + p
        else:
            break
        if (np.abs(rad) < 1 / 4):
            delta = delta / 4
        else:
            if ((np.abs(rad) > 3 / 4) and (norm(p) == delta)):
                delta = min(2 * delta, 0.1)
        radii.append(delta)
        dx = p
        y = df(x_1) - df(x)
        h = h + (np.dot(y, y.transpose())) / (np.dot(y.transpose(), dx)) - np.dot(h, np.dot(dx, np.dot(dx.transpose(), h))) / np.dot(dx.transpose(), np.dot(h, dx))
        x = x_1
        g0 = df(x)
        neval += 1
        coords.append(x)
    answer_ = [x, f(x), neval, coords, radii]
    return answer_
