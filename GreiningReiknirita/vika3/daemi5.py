import math

# Úr bókinni
def FastMultiply(x, y, n):
    if n == 1:
        return x * y
    else:
        m = math.ceil(n/2)
        a = math.floor(x/math.pow(10, m))
        b = x % pow(10, m)
        c = math.floor(y/pow(10, m))
        d = y % pow(10, m)
        e = FastMultiply(a, c, m)
        f = FastMultiply(b, d, m)
        g = FastMultiply(a-b, c-d, m)
        return (pow(10, 2*m) * e + (pow(10, m) * (e + f - g) + f))


# Úr upphaflegu greininni
def FastMultiplyOld(x, y, n):
    if n == 1:
        return x * y
    else:
        m = math.ceil(n/2)
        a = math.floor(x/math.pow(10, m))
        b = x % pow(10, m)
        c = math.floor(y/pow(10, m))
        d = y % pow(10, m)
        e = FastMultiply(a, c, m)
        f = FastMultiply(b, d, m)
        g = FastMultiply(a+b, c+d, m)
        return (pow(10, 2*m) * e + (pow(10, m) * (- e - f + g) + f))

print(FastMultiply(153, 263, 3))
print(FastMultiplyOld(153, 263, 3))