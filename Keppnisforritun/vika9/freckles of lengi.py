import math
import sys

nTest = int(sys.stdin.readline())
    
def distance(a, b):
    return math.sqrt(math.pow((b[0]-a[0]), 2) + math.pow((b[1]-a[1]), 2))

for i in range(nTest):
    _ = sys.stdin.readline()        
    n = int(sys.stdin.readline())
    adj = [set() for i in range(n)]
    lengdir = []
    hnit = []
    for j in range(n):
        data = sys.stdin.readline().split()
        a = float(data[0]); b = float(data[1])
        curr = (a,b)
        for x in hnit:
            #print("curr:", curr, " og x:", x)
            lengdir.append((abs(distance(curr, x)), curr, x))
        hnit.append((a, b))
    sorted_lengdir = sorted(lengdir, key=lambda x: x[0]) 
    utkoma = 0


    for j in range(n-1):
        #print("er ad baeta vid:", sorted_lengdir[j][0])
        utkoma = utkoma + sorted_lengdir[j][0]
    formatted_utkoma = "{:.2f}".format(utkoma)
    print(formatted_utkoma)
    #print("hnit:", hnit)
    #print("lengdir:", sorted_lengdir)

