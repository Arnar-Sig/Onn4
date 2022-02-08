from fractions import Fraction
import math
from time import time


rows, cols = (101, 20000)
geymsla = [[0]*cols]*rows
meals = [0]*rows
data = input().split()
n = int(data[0])
m = int(data[1])
data2 = input().split()
for x in range(n):
    meals[x] = int(data2[x])


print("meals:", meals)


#i=index, r=ratio af m, last=síðasta ratio
def food(capacity, courseIndex, prevCapacity):

    if courseIndex >= n:
        return 0
    if geymsla[courseIndex][capacity] == 0:
        # 1= Eat, 2= NoEat, 3= twoNoEat
        #theFood = int(min(meals[i], r))
        theFood = int(min(meals[courseIndex], capacity))
        geymsla[courseIndex][capacity] = max((food(int(capacity*Fraction(2,3)), courseIndex+1, capacity) + theFood), 
            max(food(prevCapacity, courseIndex+1, capacity), 
            food(m, courseIndex+2, capacity)))
    #print("nae i ur geymslu, [i][r]:", geymsla[i][r])
    return geymsla[courseIndex][capacity]
    
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

