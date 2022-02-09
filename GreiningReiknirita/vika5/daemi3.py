A = [0,10,15,3, 0, 1]

def MSumBrute(i, j, sum):
    if i >= j:
        return sum
    return max(MSumBrute(i+1, j, sum), MSumBrute(i+2, j, sum + A[i]))

print("MSumBrute:", MSumBrute(0, len(A), 0))

geymsla = [0 for x in range(2*len(A))]

def MSum(i, j, sum):
    orgI = i
    orgJ = j
    if i > j:
        return 0
    best = 0
    while i >= j:
        best = best + A[i]
        i += 2
    if geymsla[i] > best:
        return 0
    geymsla[i] 










# geymsla = [0 for x in range(2*len(A))]
# def MSum(i, j, sum):
#     print("i og j og sum:", i, j, sum)
#     if i >= j:
#         #print(geymsla[j-1])
#         return 0
#     # if i == j:
#     #     return geymsla[i] + sum
#     if geymsla[i] == 0:
#         geymsla[i] = max( MSum(i+1, j, sum), MSum(i+2, j, sum + A[i]))
#     else:
#         return geymsla[i]

# print("MSum:", MSum(0, len(A), 0))
    
