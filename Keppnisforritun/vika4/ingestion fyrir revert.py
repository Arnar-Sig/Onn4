import math
from time import time

rows, cols = (110, 20000)
geymsla = [[0]*cols]*rows



data = input().split(); n = int(data[0]); m = int(data[1]); data = input().split()
meals = [int(i) for i in data]
lenMeals = len(meals)

def food(i, r, last):
    if i >= lenMeals:
        return 0
    if geymsla[i][r] == 0:
        # 1= no eat, 2= two no eats, 3 = eat
        geymsla[i][r] = max(food(i+1, int(r*(2/3)), r) + min(r, meals[i]), 
        max(food(i+1, last, r)(food(i+2, m, r), 
        ))
    return geymsla[i][r]

max = food(0, m, m)
print(max)
