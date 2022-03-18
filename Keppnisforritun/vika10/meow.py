import sys

data = sys.stdin.readline()
data = int(data)
meow = 1
for i in range(1,200):
    valid = 0
    curr = data
    if curr % (pow(i,9)) == 0:
        valid = 1
    if valid == 1 and i > meow:
        meow = i
print(meow)