import math
from time import time

rows, cols = (250, 60000)
geymsla = [[0]*cols]*rows
global m
data = input().split()
n = int(data[0])
m = int(data[1])
data = input().split()
meals = [int(i) for i in data]
lenMeals = n


#i=index, r=ratio af m, last=síðasta ratio
def food(i, r, last):
    print("index:",i,"ratio:", r, "ratio*(2/3):", int(r*(2/3)), "last:", last)
    if i >= lenMeals:
        return 0
    if geymsla[i][r] == 0:
        # 1= Eat, 2= NoEat, 3= twoNoEat
        theFood = min(meals[i], r)
        geymsla[i][r] = max((food(i+1, int(r*(2/3)), r) + theFood), 
            max(food(i+1, last, r), 
            food(i+2, m, r)))
    return geymsla[i][r]
    

max = food(0, m, m)
print(max)

# 3 900
# 600 1000 1200
# kemur út 1600



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

