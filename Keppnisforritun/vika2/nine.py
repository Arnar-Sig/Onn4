def split(word):
    return [char for char in word]

board = []
count = 0
board.append(split(input()))
board.append(split(input()))
board.append(split(input()))
board.append(split(input()))
board.append(split(input()))
valid = 1

for x in board:
    if(valid == 0):
        break
    for y in x:
        if y == "k":
            count = count + 1
            firstIndex = board.index(x)
            secondIndex = x.index(y)
            #print(firstIndex, secondIndex, sep=" ")
            if (0 <= firstIndex - 2 <= 4) and 0 <= (secondIndex - 1) <= 4:
                if board[firstIndex - 2][secondIndex - 1] == "k":
                    valid = 0
                    #print("er i 1")
                    break
            if (0 <= firstIndex - 2 <= 4) and 0 <= (secondIndex + 1) <= 4:
                if board[firstIndex - 2][secondIndex + 1] == "k":
                    valid = 0
                    #print("er i 2")
                    break
            if (0 <= firstIndex - 1 <= 4) and 0 <= (secondIndex + 2) <= 4:
                if board[firstIndex - 1][secondIndex + 2] == "k":
                    valid = 0
                    #print("er i 3")
                    break
            if (0 <= firstIndex - 1 <= 4) and 0 <= (secondIndex + 2) <= 4:
                if board[firstIndex - 1][secondIndex + 2] == "k":
                    valid = 0
                    #print("er i 4")
                    break
            if (0 <= firstIndex + 1 <= 4) and 0 <= (secondIndex - 2) <= 4:
                if board[firstIndex + 1][secondIndex - 2] == "k":
                    valid = 0
                    #print("er i 5")
                    break
            if (0 <= firstIndex + 1 <= 4) and 0 <= (secondIndex + 2) <= 4:
                if board[firstIndex + 1][secondIndex + 2] == "k":
                    valid = 0
                    #print("er i 6")
                    break
            if (0 <= firstIndex + 2 <= 4) and 0 <= (secondIndex - 1) <= 4:
                if board[firstIndex + 2][secondIndex - 1] == "k":
                    valid = 0
                    #print("er i 7")
                    break
            if (0 <= firstIndex + 2 <= 4) and 0 <= (secondIndex + 1) <= 4:
                if board[firstIndex + 2][secondIndex + 1] == "k":
                    valid = 0
                    #print("er i 8")
                    break
if count != 9:
    valid = 0

if valid:
    print("valid")
else:
    print("invalid")
