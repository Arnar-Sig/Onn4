data = input().split()
solarSystemsNumber = int(data[0])
AtliShips = int(data[1])
shipsInSolarSystem = []
sigrar = 0
data = input().split()
for x in range(solarSystemsNumber):
    shipsInSolarSystem.append(int(data[x]))
shipsInSolarSystem.sort()
curr = 0
#print("Atliships: ", AtliShips)
#print("shipsinsolarsystem: ", shipsInSolarSystem)
#print("loopan byrjar:")
while curr < solarSystemsNumber and AtliShips > shipsInSolarSystem[curr]:
    #print("curr:", curr, ", shipsinsolarsystem:", shipsInSolarSystem, ", Atliships:", AtliShips)
    if shipsInSolarSystem[curr] != 0:
        AtliShips = AtliShips - shipsInSolarSystem[curr]
    else:
        AtliShips = AtliShips - 1
    sigrar = sigrar + 1
    curr = curr + 1
print(sigrar)