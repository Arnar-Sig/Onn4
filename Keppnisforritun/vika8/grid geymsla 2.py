import sys

yStaerd, xStaerd = sys.stdin.readline().split(); xStaerd = int(xStaerd); yStaerd = int(yStaerd)
adj = [set() for i in range(xStaerd)]*yStaerd
print(adj)
lengd = len(adj)
for y in range(yStaerd):
    data = sys.stdin.readline()
    for x in range(0, xStaerd):
        curr = ((y+1) * xStaerd) + x
        hopp = int(data[x])
        #print("hopp er:", hopp)
        if(hopp==x):
            continue
        if (x+1) + hopp <= xStaerd:
            adj[curr].add(curr+hopp)
            adj[curr+hopp].add(curr)
        if (x+1) - hopp >= 0:
            adj[curr].add(curr-hopp)
            adj[curr-hopp].add(curr)
        if (y+1) + hopp <= yStaerd:
            print("y+1=", y+1, " og hopp:", hopp, " og curr+(hopp*xStaerd)=", curr+(hopp*xStaerd))
            adj[curr].add(curr+(hopp*xStaerd))
            adj[curr+(hopp*xStaerd)].add(curr)
        if (y+1) - (hopp*xStaerd) >= 0:
            adj[curr].add(curr-(hopp*xStaerd))
            adj[curr-(hopp*xStaerd)].add(curr)
print(adj)





