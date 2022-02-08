A = [15, 3, 7, 4, 10, 14, 13, 12 ]
n = len(A)

def lisBigger(i,j):
    if j > n:
        return 0
    elif A[i] >= A[j]:
        return lisBigger(i, j + 1)
    else:
        skip = lisBigger(i, j + 1)
        take = lisBigger(j, j + 1)
        return max[skip, take]


print(lisBigger(-500, 0))

#gallað