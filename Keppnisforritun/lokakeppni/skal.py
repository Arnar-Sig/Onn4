from cmath import sqrt
import math
import sys

radius = sys.stdin.readline()
radius = int(radius)

ut = math.sqrt(radius*radius + radius*radius)
print(format(ut, ".6f"))