import sys

yStaerd, xStaerd = sys.stdin.readline().split(); xStaerd = int(xStaerd); yStaerd = int(yStaerd)
adj = [set() for i in range(xStaerd*yStaerd)]

lengd = len(adj)

for y in range(yStaerd):
    data = sys.stdin.readline()
    for x in range(xStaerd):
        hopp = int(data[x])
        currentStak = (y*xStaerd)+x
        hoppStaerd = hopp*xStaerd
        #hopp til hægri
        if x+hopp < xStaerd:
            #print("if 1:",currentStak, (currentStak+hopp))
            adj[currentStak].add(currentStak+hopp)
        #hopp til vinstri
        if x-hopp >= 0:
            #print("if 2:",currentStak, (currentStak-hopp))
            adj[currentStak].add(currentStak-hopp)
        #hopp upp
        if currentStak - (hoppStaerd) >= 0:
            #print("if 3:",currentStak, (currentStak-(hoppStaerd)))
            adj[currentStak].add(currentStak-(hoppStaerd))
        #hopp niður
        if currentStak + (hoppStaerd) < lengd:
            #print("if 4:",currentStak, (currentStak+(hoppStaerd)))
            adj[currentStak].add(currentStak+(hoppStaerd))
visited = [0]*lengd
queue = [0]
distance = [0]*(lengd)

distance[lengd-1] = -1
while len(queue) != 0:
    s = queue.pop(0)
    for neighbour in adj[s]:
        #print("neighbour:", neighbour)
        if visited[neighbour] == 0:
            visited[neighbour] = 1
            distance[neighbour] = distance[s] + 1
            queue.append(neighbour)




# distance[lengd-1] = -1
# while len(queue) != 0:
#     s = queue.pop(0)

#     for neighbour in adj[s]:
#         if neighbour not in visited:
#             visited.append(neighbour)
#             distance[neighbour] = distance[s] + 1
#             queue.append(neighbour)


print(distance[lengd-1])