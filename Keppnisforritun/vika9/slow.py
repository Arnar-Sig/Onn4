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
repairStation.append(nIntersection-1)
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
def dijkstra(start, adjacent, fjoldiHnuta, staerdir):
    dist = [MAXINT]*fjoldiHnuta
    prev = [-1]*fjoldiHnuta
    dist[start] = 0
    done = [0]*fjoldiHnuta
    done[start] = 1
    q = [start]
    while len(q) != 0:
        u = q.pop(0)
        for neighbour in adjacent[u]:
            if done[neighbour] == 0:
                q.append(neighbour)
                done[neighbour] = 1
            if dist[u] + staerdir[u][neighbour] < dist[neighbour]:
                #print("setting dist: u, neighbour, dist", u, neighbour, dist[u] + staerdir[u][neighbour])
                dist[neighbour] = dist[u] + staerdir[u][neighbour]
                prev[neighbour] = u
    return dist

# dijkstra á repairStations #
stationlengths = [[None for i in range(nIntersection)] for j in range(nIntersection)]
adjRepair = [set() for i in range(0, nRepair)]
for i in repairStation:
    repairDistances = dijkstra(i, adj, nIntersection, stationlengths)
    for j in repairStation:
        adjRepair[i].add(j)
        adjRepair[j].add(i)
        if stationlengths[i][j] == None and repairDistances[j] <= tireDistance:
            stationlengths[i][j] = repairDistances[j]
            stationlengths[j][i] = repairDistances[j]


startToFinish = dijkstra(0, adj, nIntersection, lengdir)
if startToFinish <= tireDistance:
    print(startToFinish)
else:
    print("er i else")
    answer = dijkstra(0, adjRepair, nRepair, repairDistances)
    print(answer(nRepair))


    






#print("dist fylkid:", dijkstra(4))

