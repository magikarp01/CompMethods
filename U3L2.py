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

def newton_raphson(f, deriv, tol, x_0):
    print("Newton-Raphson Method")
    x_f = x_0 - f(x_0)/deriv(x_0)
    iter = 0
    print(f"Iteration {iter}")
    print(f"New x is {x_f}")
    print(f"Approximate Error is {approx_error(x_0, x_f)}")
    print()

    while approx_error(x_0, x_f) > tol:
        iter+=1
        x_0 = x_f
        x_f = x_0 - f(x_0)/deriv(x_0)
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

