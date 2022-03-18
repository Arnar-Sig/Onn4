import sys
from xmlrpc.client import MAXINT
import heapq

data = sys.stdin.readline().split()
attack = int(data[0]); health = int(data[1])

data = sys.stdin.readline().split()
nCaves = int(data[0]); nEdges = int(data[1])
# attack = 5; health = 20
# nCaves = 5; nEdges = 6

adj = [set() for i in range(nCaves)]

for i in range(nEdges):
    data = sys.stdin.readline().split(); caveA = int(data[0])-1; caveB = int(data[1])-1; 
    enemyAttack = int(data[2]); enemyHealth = int(data[3])
    damage = 0
    if enemyHealth%attack == 0:
        damage = ((enemyHealth/attack)-1) * enemyAttack
    else:
        damage = (enemyHealth//attack) * enemyAttack
    if damage < health:
        adj[caveA].add((caveB, damage))

#TEST DATA #
# adj[0].add((10,1)); adj[0].add((4,2)); adj[0].add((6,3))
# adj[1].add((1,4))
# adj[2].add((0,3))
# adj[3].add((5,1))



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
    dist = [MAXINT for _ in range(n)]
    dist[root] = 0
    visited = [False for _ in range(n)]
    pq = [(0, root)]

    while len(pq) > 0:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        for v, l in graph[u]:
            #print("u:", u)
            #print("v:", v)
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))
    return dist

# print("adj:", adj)
# def lazy_dijkstras(graph, root):
#     n = len(graph)
#     dist = [MAXINT for i in range(n)]
#     dist[root] = 0
#     visited = [False for i in range(n)]
#     pq = []
#     heapq.heappush(pq, (0,0))

#     while len(pq) > 0:
#         u, _ = heapq.heappop(pq)
#         print("u er:", u, " og _ er:", _)
#         print("visited er:", visited)
#         print("distance er:", dist)
#         if visited[u]:
#             continue
#         visited[u] = True
#         for v in graph[u]:
#             #print("u:", u)
#             #print("v:", v)
#             if dist[u] + v[1] < dist[v[0]]:
#                 dist[v[0]] = dist[u] + v[1]
#                 heapq.heappush(pq, (v[0], dist[v[0]]))
#     return dist

#result = dijkstra(0, adj, nCaves, lengdir)
result = lazy_dijkstras(adj, 0)

#print("adj:", adj)
#print("result:", result)
if result[nCaves-1] >= health:
    print("Oh no")
else:
    print(int(health - result[nCaves-1]))