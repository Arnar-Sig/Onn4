#convenience föll
def split(word):
    return [char for char in word]
def printBoard(theBoard):
    for x in range(len(theBoard)):
        print(' '.join(theBoard[x]))

#gögn og vinnsla
data = input().split()
boardY = int(data[0])
boardX = int(data[1])
board = []
boulderLoc = {}; boulderLoc['x'] = 0; boulderLoc['y'] = 0
manLoc = {}; manLoc['x'] = 0; manLoc['y'] = 0
foundB = 0; foundS = 0
for x in range(boardY):
    currentLevel = split(input())
    if foundB == 0:
        if "B" in currentLevel:
            boulderLoc['y'] = x
            boulderLoc['x'] = currentLevel.index("B")
            foundB = 1
    if foundS == 0:
        if "S" in currentLevel:
            manLoc['y'] = x
            manLoc['x'] = currentLevel.index("S")
            foundS = 1
    board.append(currentLevel)

#print("board[0][1]:", board[0][1])
#print("board[1][0]:", board[1][0])
#print(manLoc)
#print(boulderLoc)

# the main
pancake = 0
direction = 0
falling = 1

while True:
    #print("BoulderLocation(y,x) - direction - falling:",boulderLoc['y'], boulderLoc['x'], direction, falling)
    #print("Board thar sem boulder er:", board[boulderLoc['x']][boulderLoc['y']])
    #print("board[boulderLoc['x']][boulderLoc['y']+1]", board[boulderLoc['x']][boulderLoc['y']+1])

    boulderBoardYplus1 = board[boulderLoc['y']+1][boulderLoc['x']]
    boulderBoard = board[boulderLoc['y']][boulderLoc['x']]

    # 1. Boulder og maður á sama stað
    if boulderLoc['y'] == manLoc['y'] and boulderLoc['x'] == manLoc['x']:
        #print("Executing if 1")
        pancake = 1
        break
    # 2. Ef rúllar til hægri og rekst á vegg \ ramp
    elif direction == "right" and (boulderBoardYplus1 == "#")  and (boulderBoard == "#" or boulderBoard == "\\"):
        #print("Executing if 2")
        pancake = 0
        break
    # 3. Ef rúllar til vinstri og rekst á vegg / ramp
    elif direction == "left" and (boulderBoardYplus1 == "#") and (boulderBoard == "#" or boulderBoard == "/"):
        #print("Executing if 3")
        pancake = 0
        break
    # 4. Ef engin stefna
    elif direction == 0 and boulderBoard == "." and falling == 1:
        #print("Executing if 4")
        pancake = 0
        break
    # 5. Ef boulder á að falla í næstu umferð
    # GALLAÐ
    elif boulderBoardYplus1 != "#":
        #print("Executing if 5")
        boulderLoc['y'] = boulderLoc['y'] + 1
        falling = 1
    # 6. Ef lendir á rampi til vinstri
    elif boulderBoard == "/" and falling == 1:
        #print("Executing if 6")
        direction = "left"
        boulderLoc['x'] -= 1
        falling = 0
    # 7. Ef lendir á rampi til hægri
    elif boulderBoard == "\\" and falling == 1:
        #print("Executing if 7")
        direction = "right"
        boulderLoc['x'] += 1
        falling = 0
    # 8. Ef einföld færlsa til hægri
    elif direction == "right":
        #print("Executing if 8")
        boulderLoc['x'] += 1
        falling = 0
    # 9. Ef einföld færsla til vinstri
    elif direction == "left":
        #print("Executing if 9")
        boulderLoc['x'] -= 1
        falling = 0
    

if pancake:
    print("Ponnukaka")
else:
    print("Heill a hufi")