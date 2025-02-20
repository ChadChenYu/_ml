import random

def hillClimbing(f, x, y, z, h = 0.01):
    while (True):
        fxyz = f(x, y, z)
        print('x = {0:.3f} y = {1:.3f} z = {2:.3f} f(x, y, z) = {3:.3f}'.format(x, y, z, fxyz))
        if f(x + h, y, z) >= fxyz:
            x = x + h
        elif f(x - h, y, z) >= fxyz:
            x = x - h
        elif f(x, y + h, z) >= fxyz:
            y = y + h
        elif f(x, y - h, z) >= fxyz:
            y = y - h
        elif f(x, y, z + h) >= fxyz:
            z = z + h
        elif f(x, y, z - h) >= fxyz:
            z = z - h
        else:
            break
    return (x, y, z, fxyz)

def f(x, y, z):
    return (x * x + y * y + z * z - 2x - 4y - 6z )

hillClimbing(f, 0, 0, 0)