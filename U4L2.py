import math

print("21.6")
def lagrange2(f, x, x0, x1, x2):
    deriv = 0
    deriv += f(x0) * (2*x-x1-x2)/((x0-x1)*(x0-x2))
    deriv += f(x1) * (2*x-x0-x2)/((x1-x0)*(x1-x2))
    deriv += f(x2) * (2*x-x0-x1)/((x2-x0)*(x2-x1))
    return deriv

def central(f, x, h, order=1, error=2):
    if order==1:
        if error==2:
            numer = f(x+h)-f(x-h)
            return numer/(2*h)
        elif error==4:
            numer = -f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h)
            return numer/(12*h)
        return -1

    elif order==2:
        if error==2:
            numer = f(x+h) - 2*f(x) + f(x-h)
            return numer/(h**2)
        elif error==4:
            numer = -f(x+2*h) + 16*f(x+h) - 30*f(x) + 16*f(x-h) - f(x-2*h)
            return numer/(12*h**2)

    return -1

y = lambda x: 2*x**4 - 6*x**3 - 12*x - 8
print(f"Lagrange approximated derivative at x=0 is {lagrange2(y, 0, -.5, 1, 2)}")
print(f"Centered difference approximation is {central(y, 0, 1)}")
print("True derivative is -12")
print()

print("21.9")
y = lambda x: 5*math.exp(-2*x) * x
deriv = lambda x: 5*(math.exp(-2*x) - 2*x*math.exp(-2*x))
print(f"Lagrange approximated derivative for x=1 is {lagrange2(y, 1, .6, 1.5, 1.6)}")
print(f"True derivative for x=1 is {deriv(1)}")
print(f"Lagrange approximated derivative for x=2 is {lagrange2(y, 2, 1.5, 1.6, 2.5)}")
print(f"True derivative for x=2 is {deriv(2)}")
print(f"Lagrange approximated derivative for x=3 is {lagrange2(y, 3, 1.6, 2.5, 3.5)}")
print(f"True derivative for x=3 is {deriv(3)}")
print()


def forward(f, x, h, error=1):
    if error == 1:
        numer = f(x+h)-f(x)
        return numer/h
    elif error==2:
        numer = - f(x+2*h) + 4*f(x+h) - 3*f(x)
        return numer/(2*h)
    return -1

def backward(f, x, h, error=1):
    return forward(f, x, -h, error=error)

print("21.19")
f = lambda x: math.exp(-2*x) - x
deriv = lambda x: -2*math.exp(-2*x) - 1
print(f"True derivative for x=2 is {deriv(2)}")
for h10 in range(5, 0, -1):
    h = h10/10
    print(f"Centered approximation for h={h} is {central(f, 2, h)}")
    print(f"Forward approximation for h={h} is {forward(f, 2, h)}")
    print(f"Backward approximation for h={h} is {backward(f, 2, h)}")