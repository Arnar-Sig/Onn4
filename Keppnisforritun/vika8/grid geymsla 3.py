import nturl2path
import sys

nBuildings, nTunnels = sys.stdin.readline().split(); nBuildings = int(nBuildings); nTunnels = int(nTunnels)

adj = [set() for i in range(nBuildings)]
lengd = len(adj)
for i in range(nTunnels):
    data = sys.stdin.readline().split(); cityA = int(data[0])-1; cityB = int(data[1])-1
    adj[cityA].add(cityB)
    adj[cityB].add(cityA)

groups = 0
visited = [0]*lengd
queue = [0]

for i in range(lengd):
    if visited[i] == 0:
        queue.append(i)
        while len(queue) != 0:
            s = queue.pop(0)
            for neighbour in adj[s]:
                if visited[neighbour] == 0:
                    visited[neighbour] = 1
                    queue.append(neighbour)
        groups += 1

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
for x in range(leggir[0]):
    if leggir[1]>0:
        #leggir[1] = leggir[1] - 1
        leggir[0] = leggir[0] - 1
        count = count + 1
    elif leggir[0] > 1:
        leggir[0] = leggir[0] - 2
        leggir[1] = leggir[1] + 2
        count = count + 1

#print("leggir[1]:", leggir[1])
if leggir[1] % 2 == 0:
    count = count + (leggir[1]/2)
else:
    count = count + (leggir[1]//2) + 1

count = int(count)
print(count + (groups-2))














#print("adj:", adj)


