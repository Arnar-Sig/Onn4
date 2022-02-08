A = [-6, 12, -7, 0, 14, -7, 5]

def MSum(i, j):
    orgI = i
    orgJ = j
    if i>j:
        return 0
    best = 0
    while i<=j:
        best = best + A[i]
        i += 1
    return max(best, MSum(orgI + 1, orgJ), MSum(orgI, orgJ-1))

print("listi A:", MSum(0, len(A)-1))

    