from math import sqrt
import random
import sys

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def happy(nr):
    summa = nr
    x = nr
    # print("summa:", summa)
    # print("nr:", nr)
    # print("x:", x)
    while summa > 9:
        summa = 0
        while x > 0:
            #print("er i lykkjunni")
            temp = x % 10
            summa += pow(temp, 2)
            x = int(x / 10)
            #print(temp, summa, x)
        if summa == 1:
            return True   
        x = summa
    if summa == 7:
        return True     
    return False

# def isPrime(n):
#     rot = sqrt(n)
#     prime = 1
#     for i in range(2,rot):
#         if n%i == 0:
#             prime = 0
#     return (prime==1)

tests = sys.stdin.readline()
for x in range(1,int(tests)+1):
    data = sys.stdin.readline().split()
    tala = int(data[1])
    if tala==1:
        print(x, tala, "NO")
        continue
    if miller_rabin(tala, 40) == False:
        print(x, tala, "NO")
        continue
    else:
        if happy(tala):
            print(x, tala, "YES")
        else:
            print(x, tala, "NO")

