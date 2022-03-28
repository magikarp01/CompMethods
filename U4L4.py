import numpy
import math

def trap_rule(f, x_l, x_u, dx=-1, segments=-1):
    sum = 0

    if segments == -1:
        numEvals = (x_u-x_l)/dx
    else:
        numEvals = segments
        dx = (x_u-x_l)/numEvals

    x2 = x_l
    for i in range(int(numEvals)):
        x1 = x2
        x2 = x1 + dx
        trapArea = dx * (f(x1)+f(x2))/2
        sum += trapArea

    return sum

# one segment simpson's rule
def seg_simpsons_rule(f, x_l, x_u, order=2):
    if order==2:
        x_m = (x_l+x_u)/2
        return (x_u-x_l)*(f(x_l) + 4*f(x_m) + f(x_u))/6
    elif order==3:
        x_1 = (2*x_l+x_u)/3
        x_2 = (x_l + 2*x_u)/3
        return (x_u-x_l) * (f(x_l) + 3*f(x_1) + 3*f(x_2) + f(x_u))/8

def simpsons_rule(f, x_l, x_u, order=2, n=1):
    dx = (x_u - x_l) / n

    sum = 0

    x2 = x_l
    for i in range(n):
        x1 = x2
        x2 = x1 + dx
        estArea = seg_simpsons_rule(f, x1, x2, order=order)
        sum += estArea

    return sum



print("Problem 2")
f = lambda x: 1-math.exp(-x)
integral = lambda x: x + math.exp(-x)
print("Analytical integral is x + e^(-x)")
ans = integral(4)-integral(1)
print(f"Answer to a. {ans}")
print(f"b. {trap_rule(f, 1, 4, segments=1)}")
