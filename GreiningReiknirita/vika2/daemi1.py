import math

def peasantIterative(x, y):
    prod = 0
    while x > 0:
        if x % 2 != 0:
            prod = prod + y
        x = math.floor(x/2)
        y = y + y
    return prod

def peasantRecursive(x, y):
    if x == 0:
        return 0
    else:
        xNew = math.floor(x/2)
        yNew = y + y
        prod = peasantRecursive(xNew, yNew)
        if x % 2 != 0:
            prod = prod + y
        return prod

print(peasantIterative(1501, 2022))
print(peasantRecursive(1501, 2022))