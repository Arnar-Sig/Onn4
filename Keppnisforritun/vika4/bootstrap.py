from cmath import sqrt
import math
import time
n = int(input())
target = n * 0.000001
x = 1
#main target = 0.000001
curr = 1
#print("er her")

while abs(pow(x, x) - n) >= target:
    while pow(x, x) < n:
        x = x + curr
 
    x = x - curr
    #if curr >= 0.000001:
    curr = curr / 10
    #print("x:", x)
    
    #print("abs:", abs(pow(x, x) - n))
    #print("current:", curr)

print(x)
