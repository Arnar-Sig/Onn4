from timeit import default_timer as timer
input_file = open('walrus1000.txt', 'r')

#inputs
n = int(input())
weights = []
for x in range(1000):
    line = input_file.readline()
    weights.append(int(line))

#geymsla = [[0]*1000]*n

#start = timer()

lausn = [False]*4000
lausn[0] = True
#print(lausn)
for x in range(len(weights)):
    check = weights[x]
    best = 2001 - check
    for y in range(best,-1, -1):
        #print("er ad finna mogulegar summur")
        if lausn[y] == True:
            #print("er ad baeta vid True")
            lausn[check+y] = True

#print("lausn[800] og lausn[1200]:", lausn[800], lausn[1200])
closest = 0
#print("len lausn:", len(lausn))
#print(lausn)
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

    











