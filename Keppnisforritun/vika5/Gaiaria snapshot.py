# convenience föll
def split(word):
    return [char for char in word]
def printBoard(theBoard):
    for x in range(len(theBoard)):
        print(' '.join(theBoard[x]))

# gögn og vinnsla
data = input().split()
boardY = int(data[0])
boardX = int(data[1])
board = []
# boulderLoc[0] = x hnit á boulder, boulderLoc[1] = y hnit á boulder!
boulderLoc = []; boulderLoc.append(0), boulderLoc.append(0)
# manLoc[0] = x hnit á manni, manLoc[1] = y hnit á manni!
manLoc = []; manLoc.append(0); manLoc.append(0)

# setja hvert "level" inn í fylkið board -> [#B..#, #\..#, ...]
# og finna hvar B=Boulder og S=maður er
foundB = 0; foundS = 0
for x in range(boardY):
    currentLevel = input()
    if foundB == 0:
        if "B" in currentLevel:
            boulderLoc[1] = x
            boulderLoc[0] = currentLevel.index("B")
            foundB = 1
    if foundS == 0:
        if "S" in currentLevel:
            manLoc[1] = x
            manLoc[0] = currentLevel.index("S")
            foundS = 1
    board.append(currentLevel)

# aðal lykkjan
pancake = 0
direction = 0
falling = 1
bouncing = 0

while True:
    print("BoulderLocation(y,x) - direction - falling - bouncing:",boulderLoc[1], boulderLoc[0], direction, falling, bouncing)
    #print("Board thar sem boulder er:", board[boulderLoc[0]][boulderLoc[1]])
    #print("board[boulderLoc[0]][boulderLoc[1]+1]", board[boulderLoc[0]][boulderLoc[1]+1])
    boulderBoardYplus1 = board[boulderLoc[1]+1][boulderLoc[0]] # reitur fyrir neðan Boulder
    boulderBoard = board[boulderLoc[1]][boulderLoc[0]]         # reitur þar sem Boulder er staðsettur

    # 1. Boulder og maður á sama stað
    if boulderLoc[1] == manLoc[1] and boulderLoc[0] == manLoc[0]:
        #print("Executing if 1")
        pancake = 1
        break
    # 2. Ef rúllar til hægri og rekst á vegg eða "\ ramp"
    elif direction == "right" and (falling == 0) and (boulderBoardYplus1 == "#")  and (boulderBoard == "#" or boulderBoard == "\\"):
        #print("Executing if 2")
        pancake = 0
        break
    # 3. Ef rúllar til vinstri og rekst á vegg eða "/ ramp"
    elif direction == "left" and (falling == 0) and (boulderBoardYplus1 == "#") and (boulderBoard == "#" or boulderBoard == "/"):
        #print("Executing if 3")
        pancake = 0
        break
    # 4. Ef engin stefna
    elif direction == 0 and boulderBoard == "." and boulderBoardYplus1 == "#" and falling == 1:
        #print("Executing if 4")
        pancake = 0
        break
 
    # 5. Ef lendir á rampi til vinstri
    elif boulderBoard == "/" and (falling == 1 or direction == "right"):
        #print("Executing if 5")
        if bouncing == 1:
            pancake = 0
            break
        direction = "left"
        boulderLoc[0] -= 1
        falling = 0
        bouncing = 1
    # 6. Ef lendir á rampi til hægri
    elif boulderBoard == "\\" and (falling == 1 or direction == "left"):
        #print("Executing if 6")
        if bouncing == 1:
            pancake = 0
            break
        direction = "right"
        boulderLoc[0] += 1
        falling = 0
        bouncing = 1

     # 7. Ef boulder á að falla í næstu umferð
    elif boulderBoardYplus1 != "#":
        #print("Executing if 7")
        boulderLoc[1] = boulderLoc[1] + 1
        falling = 1
        bouncing = 0

    # 8. Ef einföld færsla til hægri
    elif direction == "right":
        #print("Executing if 8")
        boulderLoc[0] += 1
        falling = 0
    # 9. Ef einföld færsla til vinstri
    elif direction == "left":
        #print("Executing if 9")
        boulderLoc[0] -= 1
        falling = 0
    # 10. Ef hreifist ekkert í byrjun
    elif direction == 0 and boulderBoardYplus1 == "#":
        #print("Executing if 10")
        pancake = 0
        break
    else:
        pancake = 0
        break

if pancake:
    print("Ponnukaka")
else:
    print("Heill a hufi")