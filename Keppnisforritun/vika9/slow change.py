import sys
from tracemalloc import start
from xmlrpc.client import MAXINT

# intersections, edges, Repair stations and possible distance
data = sys.stdin.readline().split()
nIntersection = int(data[0]); nEdges = int(data[1])
nRepair = int(data[2]); tireDistance = int(data[3])

# Repair stations #
repairStation = [0]
data = sys.stdin.readline().split()
for i in range(nRepair):
    repairStation.append(i)

# netið í nágrannafylki og lengdir á milli hnúta #
adj = [set() for i in range(0, nIntersection)]
lengdir = [[None for i in range(nIntersection)] for j in range(nIntersection)]


# nágrannafylki tengt með götum #
for i in range(nEdges):
    data = sys.stdin.readline().split()
    eitt = int(data[0])-1; tvo = int(data[1])-1; staerd = int(data[2])
    if staerd <= tireDistance:
        adj[eitt].add(tvo)
        adj[tvo].add(eitt)
        lengdir[eitt][tvo] = staerd
        lengdir[tvo][eitt] = staerd


# dijkstra #
def dijkstra(start):
    dist = [MAXINT]*nIntersection
    prev = [-1]*nIntersection
    dist[start] = 0
    done = [0]*nIntersection
    done[start] = 1
    q = [start]
    while len(q) != 0:
        u = q.pop(0)
        for neighbour in adj[u]:
            if done[neighbour] == 0:
                q.append(neighbour)
                done[neighbour] = 1
            if dist[u] + lengdir[u][neighbour] < dist[neighbour]:
                #print("setting dist: u, neighbour, dist", u, neighbour, dist[u] + lengdir[u][neighbour])
                dist[neighbour] = dist[u] + lengdir[u][neighbour]
                prev[neighbour] = u
    return dist[nIntersection-1]

startToFinish = dijkstra(0)
print(startToFinish)


    






#print("dist fylkid:", dijkstra(4))

