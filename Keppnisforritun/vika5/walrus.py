from timeit import default_timer as timer

n = int(input())
weights = [int(input()) for x in range(n)]
#geymsla = [[0]*2050]*n
closest = weights[0]

#start = timer()

def calc(i, j, sum):
    global closest
    if (sum > 1000) and (abs(sum-1000) > abs(closest-1000)):
        return 0
    #print("i, j og sum:", i, j, sum)
    
    if i >= j:
        #print("sum atm:", sum)
        absSum = abs(sum - 1000)
        absClos = abs(closest - 1000)
        if absSum <= absClos:
            #print("er inni")
            if absClos == absSum:
                closest = max(sum, closest)
            else:
                closest = sum
        return 0
    med = calc(i+1, j, sum + weights[i])
    an = calc(i+1, j, sum)
    return min(med, an)
    #print("er ad returna geymsla[i][sum]=", geymsla[i][sum])
calc(0, n, 0)
print(closest)
#print("geymsla:", geymsla)
#end = timer()
#print(end - start)