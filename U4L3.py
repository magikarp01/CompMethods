import numpy
import math

# x_l
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

f2 = lambda x: x*math.exp(x)
# problem 2
print(trap_rule(f2, .2, 2.2, segments=1))

# problem 3
print(trap_rule(f2, .2, 2.2, segments=3))

# problem 4
def v(t):
    if t >= 1 and t<=5:
        return 2*t
    elif t>5 and t<=14:
        return 5*t**2 + 3
print(trap_rule(v, 2, 9, segments=2))
