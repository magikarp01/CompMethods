# 6.1 and 6.2, 6.3* and 6.4*, 6.9, 6.11, 6.12
# c and d optional for 6.3, 6.4
import numpy as np
import math

def approx_error(x_i, x_f):
    return abs((x_f-x_i)/x_f)


def fixed_point(g, tol, x_0):
    print("Fixed Point Iteration")
    x_f = g(x_0)
    iter = 0
    print(f"Iteration {iter}")
    print(f"New x is {x_f}")
    print(f"Approximate Error is {approx_error(x_0, x_f)}")
    print()
    while approx_error(x_0, x_f) > tol:
        iter+=1
        x_0 = x_f
        x_f = g(x_0)
        print(f"Iteration {iter}")
        print(f"New x is {x_f}")
        print(f"Approximate Error is {approx_error(x_0, x_f)}")
        print()

def newton_raphson(f, deriv, tol, x_0, iters=-1):
    print("Newton-Raphson Method")
    x_f = x_0 - f(x_0)/deriv(x_0)
    iter = 0
    print(f"Iteration {iter}")
    print(f"New x is {x_f}")
    print(f"Approximate Error is {approx_error(x_0, x_f)}")
    print()

    if iters==-1:
        while approx_error(x_0, x_f) > tol:
            iter+=1
            x_0 = x_f
            x_f = x_0 - f(x_0)/deriv(x_0)
            print(f"Iteration {iter}")
            print(f"New x is {x_f}")
            print(f"Approximate Error is {approx_error(x_0, x_f)}")
            print()

    else:
        for i in range(iters):
            iter += 1
            x_0 = x_f
            x_f = x_0 - f(x_0) / deriv(x_0)
            print(f"Iteration {iter}")
            print(f"New x is {x_f}")
            print(f"Approximate Error is {approx_error(x_0, x_f)}")
            print()

def secant_method(f, tol, x_0, x_1, iters=-1):
    print("Secant Method")
    x_2 = f(x_1)*(x_0-x_1)/(f(x_0) - f(x_1))
    iter = 0
    print(f"Iteration {iter}")
    print(f"New x is {x_2}")
    print(f"Approximate Error is {approx_error(x_1, x_2)}")
    print()
    if iter == -1:
        while approx_error(x_1, x_2) > tol:
            iter += 1
            x_0 = x_1
            x_1 = x_2
            x_2 = f(x_1)*(x_0-x_1)/(f(x_0) - f(x_1))
            print(f"Iteration {iter}")
            print(f"New x is {x_2}")
            print(f"Approximate Error is {approx_error(x_1, x_2)}")
            print()

    else:
        for i in range(iters):
            iter += 1
            x_0 = x_1
            x_1 = x_2
            x_2 = f(x_1) * (x_0 - x_1) / (f(x_0) - f(x_1))
            print(f"Iteration {iter}")
            print(f"New x is {x_2}")
            print(f"Approximate Error is {approx_error(x_1, x_2)}")
            print()

def modified_secant(f, tol, delta, x_0, iters=-1):
    print("Newton-Raphson Method")
    x_f = x_0 - delta * x_0 * f(x_0) / (f(x_0 + delta*x_0) - f(x_0))
    iter = 0
    print(f"Iteration {iter}")
    print(f"New x is {x_f}")
    print(f"Approximate Error is {approx_error(x_0, x_f)}")
    print()

    if iters == -1:
        while approx_error(x_0, x_f) > tol:
            iter += 1
            x_0 = x_f
            x_f = x_f = x_0 - delta * x_0 * f(x_0) / (f(x_0 + delta*x_0) - f(x_0))
            print(f"Iteration {iter}")
            print(f"New x is {x_f}")
            print(f"Approximate Error is {approx_error(x_0, x_f)}")
            print()

    else:
        for i in range(iters):
            iter += 1
            x_0 = x_f
            x_f = x_f = x_0 - delta * x_0 * f(x_0) / (f(x_0 + delta * x_0) - f(x_0))
            print(f"Iteration {iter}")
            print(f"New x is {x_f}")
            print(f"Approximate Error is {approx_error(x_0, x_f)}")
            print()



print("Problem 6.1")
g = lambda x: math.sin(math.sqrt(x))
fixed_point(g, .0001, .5)

print("Problem 6.2")
f = lambda x: -.9*x*x + 1.7*x + 2.5
deriv = lambda x: -1.8*x + 1.7
g = lambda x: (-.9*x*x + 2.5)/1.7
print("Part A:")
fixed_point(g, .0001, 5)
print("Part B:")
newton_raphson(f, deriv, .0001, 5)

print("Problem 6.3")
f = lambda x: x**3 - 6*x*x + 11*x - 6.1
print("Graphically: by Desmos, 3.047")
print("Part B: ")
