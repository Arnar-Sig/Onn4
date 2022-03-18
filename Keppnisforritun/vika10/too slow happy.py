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
        digit = [int(d) for d in str(tala)]
        strengur = "-1"
        nytt = 0
        summa = 0
        #print("strengur fyrir lykkju:", strengur)
        while (int(strengur) != 1) and (int(strengur) != tala):
            #print("digit er nuna:", digit)
            #print("strengur:", strengur)
            nytt = 0
            summa = 0
            for i in range(len(digit)):
                nytt = nytt + pow(digit[i], 2)
            strengur = str(nytt)
            digit = [int(d) for d in str(nytt)]
                
        strengur = ''.join(map(str,digit))
        if int(strengur) == 1:
            print(x, tala, "YES")
        else:
            print(x, tala, "NO")

