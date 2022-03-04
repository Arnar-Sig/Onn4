import sys
y, x =sys.stdin.readline().split(); x = int(x); y = int(y)
adj = [[set() for i in range(x)]]*y
print(adj)