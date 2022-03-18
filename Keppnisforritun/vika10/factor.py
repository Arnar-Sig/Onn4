from functools import reduce
import math
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








tests = sys.stdin.readline(); tests = int(tests)
for i in range(tests):
    #print("naeasta tala:")
    dataOrg = sys.stdin.readline(); data = int(dataOrg)
    rot = math.sqrt(data)
    if rot == int(rot) and data != int(rot):
        if miller_rabin(int(rot), 40):
            print(dataOrg)

