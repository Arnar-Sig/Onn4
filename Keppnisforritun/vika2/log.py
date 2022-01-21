noArtists = int(input())
list = [[] for x in range(noArtists)]
for x in list:
    n = int(input())
    for y in range(n+1):
        x.append(input())

outcome = []

for x in list:
    outcome.append((x[0] + ":"))
    matchingSongs = []
    for y in range(1, len(x)):
        if len(x[y]) - x[y].count(' ') == (len(x[0]) - x[0].count(' ')):
            matchingSongs.append(x[y])
            #outcome.append(x[y])
    matchingSongs.sort()
    for z in matchingSongs:
        outcome.append(z)        
    
for x in outcome:
    print(x)











# data = []
# for x in range(noArtists):
#     n = int(input()) # number of songs
#     data.append(n)
#     for x in range(n + 1):
#         data.append(input())
    
# print(data)
# navigator = 2
# nextBreak = data[0] + 2
# currentBand = data[1]
# outcome = []
# for y in range(noArtists):
#     listOfSongs = []
#     while navigator < nextBreak:
#         print("er her!")
#         print(data[navigator])
#         if len(data[navigator]) - data[navigator].count(' ') == len(currentBand) - currentBand.count(' '):
#             listOfSongs.append(data[navigator])
#         navigator = navigator + 1
#     print("komst ut!")
#     nextBreak = int(nextBreak) + int(data[nextBreak + 2]) + 1
#     currentBand = data[navigator + 1]
#     listOfSongs.sort()
#     outcome.append(currentBand)
#     for x in listOfSongs:
#         outcome.append(x)
    
# print(outcome)

