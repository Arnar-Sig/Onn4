import math
from time import time
data = input().split(); n = int(data[0]); m = int(data[1]); data = input().split()
meals = [int(i) for i in data]
lenMeals = len(meals)
ratio = [1]; temp = 1
for x in range(lenMeals):
    temp = temp * (2/3)
    ratio.append(temp)

def food(i, timeSince, r, sum):
    if i == lenMeals:
        return sum
    else:
        if timeSince >= 1:
            noEat = food(i+1, timeSince+1, 0, sum)
        else:
            noEat = food(i+1, timeSince+1, r-1, sum)
        if m*ratio[r] >= meals[i]:
            eat = food(i+1, 0, r+1, sum + math.floor(meals[i]))
        else:
            eat = food(i+1, 0, r+1, sum + math.floor(m*ratio[r]))
        return max(eat, noEat)

max = food(0,2,0,0)
print(max)
