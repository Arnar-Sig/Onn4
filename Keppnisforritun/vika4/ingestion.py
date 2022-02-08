from fractions import Fraction
import math
from time import time

rows, cols = (200, 60000)
geymsla = [[0]*cols]*rows

data = input().split()
n = int(data[0])
m = int(data[1])
data = input().split()
meals = [int(i) for i in data]


#print("meals:", meals)


#i=index, r=ratio af m, last=síðasta ratio
def food(r, i, last):
    #print("index:",i,"ratio:", r, "ratio*(2/3):", int(r*(2/3)), "last:", last)
    if i >= n:
        return 0
    if geymsla[i][r] == 0:
        # 1= Eat, 2= NoEat, 3= twoNoEat
        theFood = int(min(meals[i], r))
        geymsla[i][r] = max((food(int(r*2/3),i + 1, r) + min(meals[i], r)), 
                max(food(last, i + 1, r), food( m, i + 2, r)))
    #print("nae i ur geymslu, [i][r]:", geymsla[i][r])
    return geymsla[i][r]
    

max = food(m, 0, m)

print(max)

# 3 900
# 400 1000 1500
# kemur rangt út














# ratio = [1]; temp = 1
# for x in range(lenMeals):
#     temp = temp * (2/3)
#     ratio.append(temp)

# def food(i, timeSince, r, sum):
#     if i == lenMeals:
#         return sum
#     else:
#         if timeSince >= 1:
#             noEat = food(i+1, timeSince+1, 0, sum)
#         else:
#             noEat = food(i+1, timeSince+1, r-1, sum)
#         if m*ratio[r] >= meals[i]:
#             eat = food(i+1, 0, r+1, sum + math.floor(meals[i]))
#         else:
#             eat = food(i+1, 0, r+1, sum + math.floor(m*ratio[r]))
#         return max(eat, noEat)

# max = food(0,2,0,0)
# print(max)

