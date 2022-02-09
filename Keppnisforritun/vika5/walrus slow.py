n = int(input())
weights = [int(input()) for x in range(n)]
geymsla = [[0]*2000]*20
closest = 0

def calc(i, j, sum):
    global closest
    if i >= j:
        print("sum atm:", sum)
        if abs(sum - 1000) < abs(closest - 1000):
            closest = sum
        return 0
    else:
        med = calc(i+1, j, sum + weights[i])
        an = calc(i+1, j, sum)
        return min(med, an)


calc(0, n, 0)
print(closest)
#print("geymsla:", geymsla)