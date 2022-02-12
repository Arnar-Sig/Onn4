
def isWord(i, j):
    print("hi)")
n = 1
A = []

def splittable(i, sum):
    if i > n:
        return sum
    j = i
    for j in range(n):
        if isWord(i, j):
            if splittable(j+1, sum):
                return (sum + 1)
    return 0


def fastSplittable(A):
    n = len(A)
    SplitTable = [0 for x in range(n)]
    SplitTable.append(1)
    i = n
    for i in range(n, i, -1):
        if isWord(i, j) and SplitTable[j+1] > 0:
            SplitTable[i] = SplitTable[j+1] + 1
    return SplitTable[1]


