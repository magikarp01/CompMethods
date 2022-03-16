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
    print("Modified Secant Method")
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
deriv = lambda x: 3*x**2 - 12*x + 11
print("Graphically: by Desmos, 3.047")
print("Part B: ")
newton_raphson(f, deriv, -1, 3.5, iters=3)
print("Part C: ")
secant_method(f, -1, 2.5, 3.5, iters=3)
print("Part D: ")
modified_secant(f, -1, .01, 3.5, iters=3)


print("Problem 6.4")
f = lambda x: 7*math.sin(x) * math.exp(-x) - 1
deriv = lambda x: 7* (math.cos(x) * math.exp(-x) - math.sin(x)*math.exp(-x))
print("Graphically: by Desmos, 0.17")
print("Part B: ")
newton_raphson(f, deriv, -1, .3, iters=3)
print("Part C: ")
secant_method(f, -1, .5, .4, iters=3)
print("Part D: ")
modified_secant(f, -1, .01, .2, iters=5)


print("Problem 6.9")
f = lambda x: -2 + 6*x - 4*x*x + .5*x*x*x
deriv = lambda x: 6 - 8*x + 1.5*x*x
print("Part A:")
newton_raphson(f, deriv, .01, 4.5)
print("Part B:")
newton_raphson(f, deriv, .01, 4.43)
print("Difference is because the function has multiple roots.")


print("Problem 6.11")
f = lambda x: math.tanh(x*x - 9)
deriv = lambda x: 2*x/((math.cosh(x*x-9))**2)
newton_raphson(f, deriv, -1, 3.2, iters=2)


print("Problem 6.12")
f = lambda x: 0.0074*x**4 - .284*x**3 + 3.355*x**2 - 12.183*x + 5
deriv = lambda x: .0296*x**3 - .852*x**2 + 6.71*x - 12.183
newton_raphson(f, deriv, .01, 16.15, iters=10)
print("Doesn't find the root between 15 and 20 because of slope, 16.15 doesn't iterate into that range")


