import sys
from xmlrpc.client import MAXINT
import heapq

data = sys.stdin.readline().split()
attack = int(data[0]); health = int(data[1])

data = sys.stdin.readline().split()
nCaves = int(data[0]); nEdges = int(data[1])

adj = [set() for i in range(nCaves)]
lengdir = [[None for i in range(nCaves)] for j in range(nCaves)]
for i in range(nEdges):
    data = sys.stdin.readline().split(); caveA = int(data[0])-1; caveB = int(data[1])-1; 
    enemyAttack = int(data[2]); enemyHealth = int(data[3])
    damage = 0
    if enemyHealth%attack == 0:
        damage = ((enemyHealth/attack)-1) * enemyAttack
    else:
        damage = (enemyHealth//attack) * enemyAttack
    if damage < health:
        adj[caveA].add(caveB)
        adj[caveB].add(caveA)
        lengdir[caveA][caveB] = damage
        lengdir[caveB][caveA] = damage

# def dijkstra(start, adjacent, fjoldiHnuta, staerdir):
#     dist = [MAXINT]*fjoldiHnuta
#     dist[start] = 0
#     done = [0]*fjoldiHnuta
#     done[start] = 1
#     q = []
#     for i in range(fjoldiHnuta):
#         heapq.heappush(q, i)
#     while len(q) != 0:
#         u = heapq.heappop(q)
#         for neighbour in adjacent[u]:
#             if done[neighbour] == 0:
#                 #q.append(neighbour)
#                 heapq.heappush(q, neighbour)
#                 done[neighbour] = 1
#             if dist[u] + staerdir[u][neighbour] < dist[neighbour]:
#                 dist[neighbour] = dist[u] + staerdir[u][neighbour]
#     return dist


def lazy_dijkstras(graph, root):
    n = len(graph)
    # set up "inf" distances
    dist = [MAXINT for _ in range(n)]
    # set up root distance
    dist[root] = 0
    # set up visited node list
    visited = [False for _ in range(n)]
    # set up priority queue
    pq = [(0, root)]
    # while there are nodes to process
    while len(pq) > 0:
        # get the root, discard current distance
        _, u = heapq.heappop(pq)
        # if the node is visited, skip
        if visited[u]:
            continue
        # set the node to visited
        visited[u] = True
        # check the distance and node and distance
        for v, l in graph[u]:
            # if the current node's distance + distance to the node we're visiting
            # is less than the distance of the node we're visiting on file
            # replace that distance and push the node we're visiting into the priority queue
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))
    return dist

#result = dijkstra(0, adj, nCaves, lengdir)
result = lazy_dijkstras(adj, 0)
#print("adj:", adj)
#print("lengdir", lengdir)
#print("result:", result)
if result[nCaves-1] >= health:
    print("Oh no")
else:
    print(int(health - result[nCaves-1]))