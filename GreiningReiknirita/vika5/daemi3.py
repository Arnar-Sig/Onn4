A = [16, -15, -4, 10, 5, 8, 0, -1, -12, -8, 3, 20, -11, 6, 4, 11, -10, -2, -7, -9, 13, -3, 18, 1, 7]
A3 = [3, 15, -7, 8, 1]
A2 = [0,10,15,3, 0, 1]

# Brute force
def MSumBrute(i, j, sum):
    if i >= j:
        return sum
    return max(MSumBrute(i+1, j, sum), MSumBrute(i+2, j, sum + A[i]))

#print("MSumBrute:", MSumBrute(0, len(A), 0))


geymsla = [0 for x in range(len(A)+1)]
geymsla[0] = 0

def MSum(i, j, sum):
    if i >= j:
        return geymsla[0]
    if geymsla[i] == 0:
        geymsla[i] = max(MSum(i+1, j, sum), MSum(i+2, j, sum + A[i]))
    #print("returna geymsla[i]:", geymsla[i])
    if geymsla[i] > sum:
        return geymsla[i]
    else:
        return geymsla[i] + sum
    
#print(geymsla)




print("MSum:", MSum(0, len(A), 0))









# def MSum(i, j, sum):
#     for i in range(1, len(geymsla)):
#         geymsla[i] = max(geymsla[i-1]+ A[i-1], )

# print("MSum:", MSum(0, len(A), 0))
# print("geymsla:", geymsla)












# #næstum
# def MSum(i, j, sum):
#     print("sum:", sum)
#     if i >= j:
#         best = 0
#         for x in range(len(geymsla)):
#             if geymsla[x] > best:
#                 besst = geymsla[x]
#         return best
        
#     if i == j-1:
#         if geymsla[j-1] < sum + A[i]:
#             geymsla[j-1] = sum + A[i]
#         best = 0
#         for x in range(len(geymsla)):
#             if geymsla[x] > best:
#                 besst = geymsla[x]
#         return best
#     if geymsla[i] == 0:
#         geymsla[i] = max(MSum(i+1, j, sum), MSum(i+2, j, sum + A[i]))
#     return geymsla[i]

# print("MSum:", MSum(0, len(A), 0))
# print("geymsla:", geymsla)


















# def MSum(i, j, sum):
#     if i > j:
#         return 0
#     best = 0
#     while i >= j:
#         best = best + A[i]
#         i += 2
#     if geymsla[i] > best:
#         return 0

#     geymsla[i] = best

# print("MSum:", MSum(0, len(A), 0))


























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
    
