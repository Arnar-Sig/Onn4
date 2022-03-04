import sys
from xmlrpc.client import MAXINT

testcase = int(sys.stdin.readline())
for x in range(testcase):
    data = sys.stdin.readline().split(); cities = int(data[0]); pilots = int(data[1])
    adj = [set() for i in range(cities)]
    #print(adj)
    for i in range(pilots):
        data = sys.stdin.readline().split(); cityA = int(data[0])-1; cityB = int(data[1])-1
        adj[cityA].add(cityB)
        adj[cityB].add(cityA)
    #shortest = MAXINT
    visited = [0]
    #print(adj)
    queue = [0]
    count = 0
    while len(queue) != 0:
        
        s = queue.pop(0)
        #print(s)
        for neighbour in adj[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                count += 1

    print(count)