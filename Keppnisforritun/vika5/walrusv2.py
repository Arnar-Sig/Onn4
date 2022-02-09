n = int(input())
weights = [int(input()) for x in range(n)]
#geymsla = [[0]*1000]*n

lausn = [False]*2001
lausn[0] = True
#print(lausn)
for x in range(len(weights)):
    curr = weights[x]
    max = 2001 - curr
    for y in range(max):
        if lausn[y] == True:
            lausn[y + curr] = True

#print("lausn[800] og lausn[1200]:", lausn[800], lausn[1200])
closest = 0
#print("len lausn:", len(lausn))
for x in range(len(lausn)):
    #print("x er:", x)
    if lausn[x] == True:
        absLausn= abs(x - 1000)
        absClos = abs(closest - 1000)
        if absLausn <= absClos:
            closest = x
        # elif absClos == absLausn:
        #     closest = max(x, closest)
print(closest)

    











