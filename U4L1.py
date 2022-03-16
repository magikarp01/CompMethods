import math

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

print("Problem 21.1")
f = lambda x: math.sin(x)
x_0 = math.pi/4
h = math.pi/12

print(f"Forward error 1: {forward(f, x_0, h, error=1)}")
print(f"Forward error 2: {forward(f, x_0, h, error=2)}")
print(f"Backward error 1: {backward(f, x_0, h, error=1)}")
print(f"Backward error 2: {forward(f, x_0, h, error=2)}")
print(f"Central error 2: {central(f, x_0, h, error=2)}")
print(f"Central error 4: {central(f, x_0, h, error=4)}")
print()

print("Problem 21.2")
f = lambda x: math.exp(x)
x_0 = 2
h = .1
print(f"Central order 1 error 2: {central(f, x_0, h, order=1, error=2)}")
print(f"Central order 1 error 4: {central(f, x_0, h, order=1, error=4)}")
print(f"Central order 2 error 2: {central(f, x_0, h, order=2, error=2)}")
print(f"Central order 2 error 4: {central(f, x_0, h, order=2, error=4)}")