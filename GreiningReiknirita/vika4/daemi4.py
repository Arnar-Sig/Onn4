def LIS(A):
    best = 0
    n = len(A)
    for i in range(n):
        best = max(best, LISfirst(A, i, n))
    return best

def LISfirst(A, i, n):
    best = 0
    j = i + 1
    while j < n:
        if A[j] > A[i]:
            best = max(best, LISfirst(A, j, n))
        j = j + 1
    return 1 + best

listinn = [2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, 9, 0, 4, 5, 2, 3, 5, 3]
print(LIS(listinn))

