from timeit import default_timer as timer

#inputs
n = int(input())
weights = [int(input()) for x in range(n)]
#geymsla = [[0]*1000]*n

#start = timer()

lausn = [False]*4000
lausn[0] = True
for x in range(len(weights)):
    check = weights[x]
    best = 2001 - check
    for y in range(best,-1, -1):
        if lausn[y] == True:
            lausn[check+y] = True
closest = 0
for x in range(len(lausn)):
    #print("x er:", x)
    if lausn[x] == True:
        absX = abs(x-1000); absClos = abs(closest-1000)
        if absX <= absClos:
            #print("checking lausn[x]:", lausn[x])
            #print("abs(x-1000):", abs(x-1000))
            #print("abs(closest-1000):", abs(closest-1000))
            closest = x
        if absX == absClos:
            closest = max(x, closest)
            continue

print(closest)
#end = timer()
#print(end - start)

    











