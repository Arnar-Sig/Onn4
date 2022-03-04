import sys

yStaerd, xStaerd = sys.stdin.readline().split(); xStaerd = int(xStaerd); yStaerd = int(yStaerd)
adj = [set() for i in range(xStaerd)]*yStaerd
print(adj)
lengd = len(adj)
for y in range(0, lengd, xStaerd):
    data = sys.stdin.readline()
    for x in range(0, xStaerd):
        curr = int(data[x])
        print("curr er:", curr)
        if(curr==x):
            continue
        if curr + curr <= xStaerd:
            adj[curr].add(curr+curr)
            adj[curr+curr].add(curr)
        if curr - curr >= 0:
            adj[curr].add(curr-curr)
            adj[curr-curr].add(curr)
        if curr + (curr*xStaerd) <= yStaerd:
            adj[curr].add(curr+(curr*xStaerd))
            adj[curr+(curr*xStaerd)].add(curr)
        if curr - (curr*xStaerd) >= 0:
            adj[curr].add(curr-(curr*xStaerd))
            adj[curr-(curr*xStaerd)].add(curr)
print(adj)





