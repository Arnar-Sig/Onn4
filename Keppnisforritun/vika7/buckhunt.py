import sys
sight = sys.stdin.readline().split()
n = int(sys.stdin.readline())
count = 0


for i in range(n):
    data = input().split()
    
    if int(data[0]) >= int(sight[0]) and int(data[0]) <= int(sight[1]) and int(data[1]) >= int(sight[2]) and int(data[1]) <= int(sight[3]):
        count += 1
print(count)