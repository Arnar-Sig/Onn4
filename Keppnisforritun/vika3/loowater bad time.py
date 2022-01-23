import sys
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
   
    
    if dragonHeadsNumber > knightsNumber:
        possible = 0
    
    #print("dragonheads: ", dragonheads)
    #print("knights: ", knights)
    goldcoins = 0
    validKnights = 0
    possible = 1
    for x in dragonheads:
        min = sys.maxsize
        minKnight = -1
        for y in knights:
            if y >= x and (y - x) <= min:
                min = (y - x)
                #print("y-x =", y-x, " í knight: ", y, " og current min: ", min)
                minKnight = y
                
        if min != sys.maxsize:
            validKnights = validKnights + 1
            goldcoins = goldcoins + minKnight
            knights.remove(minKnight)
        else:
            possible = 0
            break
        
    if validKnights < dragonHeadsNumber:
        possible = 0
    
    if possible == 1:
        print(goldcoins)
    else:
        print("Loowater is doomed!")