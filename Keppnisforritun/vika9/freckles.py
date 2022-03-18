import math
import sys

nTest = int(sys.stdin.readline())
    
def distance(a, b):
    return math.sqrt(math.pow((b[0]-a[0]), 2) + math.pow((b[1]-a[1]), 2))

for i in range(nTest):
    _ = sys.stdin.readline()        
    n = int(sys.stdin.readline())

