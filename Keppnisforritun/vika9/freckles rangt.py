import heapq
import math
import sys
from xmlrpc.client import MAXINT

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

def distance(a, b):
    return math.sqrt(math.pow((b[0]-a[0]), 2) + math.pow((b[1]-a[1]), 2))

nTest = int(sys.stdin.readline())

for i in range(nTest):
    _ = sys.stdin.readline()
    n = int(sys.stdin.readline())
    adj = [set() for i in range(n)]
    hnutar = []
    for j in range(n):
        data = sys.stdin.readline().split()
        a = float(data[0]); b = float(data[1])
        curr = (a,b)
        hnutar.append((j, curr, MAXINT))
    for j in range(len(hnutar)):
        for k in range(len(hnutar)):
            adj[j].add(hnutar[k])
            adj[k].add(hnutar[j])
    

            


    # utkoma = 0
    # for j in range(n-1):
    #     utkoma = utkoma + lengdir[j]
    # formatted_utkoma = "{:.2f}".format(utkoma)
    # print(formatted_utkoma)
    
    # print("hnit:", hnit)
    # print("lengdir:", lengdir)
