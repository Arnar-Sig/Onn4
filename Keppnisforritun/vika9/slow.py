import readline
import sys

# intersections, edges, Repair stations and possible distance
data = sys.stdin.readline().split()
nIntersection = int(data[0]); nEdges = int(data[1])
nRepair = int(data[2]); tireDistance = int(data[3])

# Repair stations
repairStation = [0]*(nIntersection)
data = sys.stdin.readline().split()
for i in range(nRepair):
    repairStation[int(data[i])] = 1

# netið í nágrannafylki
adj = [set() for i in range(0, nIntersection)]

# nágrannafylki tengt með götum
for i in range(nEdges):
    data = sys.stdin.readline().split()
    eitt = int(data[0])-1; tvo = int(data[1])-1; thrju = int(data[2])-1
    adj[eitt].add(tvo)
    adj[tvo].add(eitt)
    adj[tvo].add(thrju)
    adj[thrju].add(tvo)
#print(adj)
