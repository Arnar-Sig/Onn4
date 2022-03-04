import nturl2path
import sys

nBuildings, nTunnels = sys.stdin.readline().split(); nBuildings = int(nBuildings); nTunnels = int(nTunnels)

adj = [set() for i in range(nBuildings)]
lengd = len(adj)
for i in range(nTunnels):
    data = sys.stdin.readline().split(); cityA = int(data[0])-1; cityB = int(data[1])-1
    adj[cityA].add(cityB)
    adj[cityB].add(cityA)

leggir = [0, 0]
lengd = len(adj)
for i in range(lengd):
    #print("len(adj[i]):", len(adj[i]))
    if len(adj[i]) == 0:
        leggir[0] = leggir[0] + 1
    elif len(adj[i]) == 1:
        leggir[1] = leggir[1] + 1
#print("leggir[1]:", leggir[1])
count = 0
while leggir[0] != 0:
    if leggir[1]>0:
        #leggir[1] = leggir[1] - 1
        leggir[0] = leggir[0] - 1
        count = count + 1
    elif leggir[0] > 1:
        leggir[0] = leggir[0] - 2
        leggir[1] = leggir[1] + 2
        count = count + 1
    else:
        break
#print("leggir[1]:", leggir[1])
if leggir[1] % 2 == 0:
    count = count + (leggir[1]/2)
else:
    count = count + (leggir[1]//2) + 1

count = int(count)
print(count)














#print("adj:", adj)


