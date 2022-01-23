def binSearch(listi, x):
    if len(listi)==1:
        return 0
    min = 0
    max = len(listi) -1
    while min <= max:
        mid = min + (max - min) // 2
        if listi[mid] < x:
            min = mid + 1
        elif listi[mid] > x:
            max = mid - 1
        else:
            if listi[mid] == x:
                return mid
    if listi[mid] < x:
        return (mid + 1)
    else:
        return mid




while True:
    data = input().split()
    if data == ["0", "0"]:
        break
    dragonheads = []
    dragonHeadsNumber = int(data[0])
    knights = []
    knightsNumber = int(data[1])
    for x in range(dragonHeadsNumber):
        inntak = int(input())
        dragonheads.append(inntak)
    for x in range(knightsNumber):
        inntak = int(input())
        knights.append(inntak)
    dragonheads.sort(reverse=True)
    knights.sort()
    possible = 1
    if dragonHeadsNumber > knightsNumber:
        possible = 0
    #print("dragonheads: ", dragonheads)
    #print("knights: ", knights)
    goldcoins = 0
    #validKnights = 0
    if possible == 1:
        for x in dragonheads:
            #print("er i dragonhead: ", x)
            last = knights[-1]
            if last < x:
                possible = 0
                break
            else:
                best = binSearch(knights, x)
                #print("current knights: ", knights, " og current best: ", best)
                goldcoins = goldcoins + knights[best]
                knights.remove(knights[best])
    # if validKnights < dragonHeadsNumber:
    #     possible = 0
    if possible == 1:
        print(goldcoins)
    else:
        print("Loowater is doomed!")