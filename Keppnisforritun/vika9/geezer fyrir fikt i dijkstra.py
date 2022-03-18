from math import ceil, floor
import sys
from xmlrpc.client import MAXINT

# data = sys.stdin.readline().split()
# attack = int(data[0]); health = int(data[1])
attack = 5; health = 20

# data = sys.stdin.readline().split()
# nCaves = int(data[0]); nEdges = int(data[1])
nCaves = 5; nEdges = 6

adj = [set() for i in range(nCaves)]
lengdir = [[None for i in range(nCaves)] for j in range(nCaves)]
# for i in range(nEdges):
#     data = sys.stdin.readline().split(); caveA = int(data[0])-1; caveB = int(data[1])-1; 
#     enemyAttack = int(data[2]); enemyHealth = int(data[3])
#     damage = 0
#     if enemyHealth%attack == 0:
#         damage = ((enemyHealth/attack)-1) * enemyAttack
#     else:
#         damage = floor(enemyHealth/attack) * enemyAttack
#     if damage < health:
#         adj[caveA].add(caveB)
#         adj[caveB].add(caveA)
#         lengdir[caveA][caveB] = damage
#         lengdir[caveB][caveA] = damage

#TEST DATA #
adj[0].add(1); adj[0].add(2); adj[0].add(3)
adj[1].add(4)
adj[2].add(3)
adj[3].add(1)
lengdir[0][1] = 10; lengdir[1][0] = 10
lengdir[0][2] = 4; lengdir[2][0] = 4
lengdir[0][3] = 6; lengdir[3][0] = 6
lengdir[1][4] = 1; lengdir[4][1] = 1
lengdir[2][3] = 0; lengdir[3][2] = 0
lengdir[3][1] = 5; lengdir[1][3] = 5


def dijkstra(start, adjacent, fjoldiHnuta, staerdir):
    dist = [MAXINT]*fjoldiHnuta
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
    return dist
print("adj:", adj)
print("lengdir", lengdir)

result = dijkstra(0, adj, nCaves, lengdir)
print(result)