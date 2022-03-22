import math
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
# I chose problem 6.25, Manning Equation

def manning(H, S=.0002, B=20, n=.03):
    num = math.sqrt(S) * ((B*H)**(5/3))
    denom = n* ((B + 2*H)**(2/3))
    return num/denom

# xData = np.linspace(0, 2, 1000)
# yData = [manning(x)-5 for x in xData]
# plt.plot(xData, yData)
# plt.title("Q-5 plotted against H according to Manning Equation")
# plt.xlabel("Value of H")
# plt.show()

def approx_error(x_i, x_f):
    return abs((x_f-x_i)/x_f)

def bisection(f, x_l, x_u, tol):

    oldX = 0
    x = (x_l+x_u)/2
    val = f(x)
    print(f"Approximation of root is {x}, Value is {val}")

    approximations = [x]
    errors = [approx_error(oldX, x)]

    while approx_error(oldX, x)>tol:
        oldX = x
        if val < 0:
            x_l = x
        else:
            x_u = x
        x = (x_l+x_u)/2
        val = f(x)
        print(f"Approximation of root is {x}, Value is {val}")
        approximations.append(x)
        errors.append(approx_error(oldX, x))

    return approximations, errors


def modified_secant(f, tol, delta, x_0):
    print("Modified Secant Method")
    x_f = x_0 - delta * x_0 * f(x_0) / (f(x_0 + delta*x_0) - f(x_0))
    iter = 1
    print(f"Iteration {iter}")
    print(f"New x is {x_f}")
    print(f"Approximate Error is {approx_error(x_0, x_f)}")
    print()

    approximations = [x_f]
    errors = [approx_error(x_0, x_f)]
    while approx_error(x_0, x_f) > tol:
        iter += 1
        x_0 = x_f
        x_f = x_f = x_0 - delta * x_0 * f(x_0) / (f(x_0 + delta*x_0) - f(x_0))
        print(f"Iteration {iter}")
        print(f"New x is {x_f}")
        print(f"Approximate Error is {approx_error(x_0, x_f)}")
        print()
        approximations.append(x_f)
        errors.append(approx_error(x_0, x_f))

    return approximations, errors


# approximations, errors = bisection(lambda x:manning(x)-5, .5, 1, .0005)
# approximations, errors = bisection(lambda x:manning(x)-5, .25, 2, .0005)
# approximations, errors = modified_secant(lambda x:manning(x)-5, .0005, .001, .5)
approximations, errors = modified_secant(lambda x:manning(x)-5, .0005, .02, 1.5)

funcValues = [manning(x)-5 for x in approximations]
iterations = list(range(1, len(approximations)+1))
iterations.insert(0, "Iteration")
approximations.insert(0, "Approximation")
funcValues.insert(0, "Function Value")
errors.insert(0, "Relative Error")
print(tabulate(np.transpose([iterations, approximations, funcValues, errors])))
