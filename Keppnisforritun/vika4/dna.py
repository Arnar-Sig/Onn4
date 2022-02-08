# breytur etc
n = int(input())
data = input()
dna = [i for i in data]
rows, cols = (n, 20000)
geymsla = [[0]*cols]*rows

# 1= A til vinstri, 2= B til vinstri
def fall(i, moves):
    if i == 1:
        return moves
    if geymsla[i][moves]:






if n == 1:
    print(0)
else:
    print(fall(n-1, 0))










# ### swap fallið ###
# def swap(listi, k):
#     for i in range(k + 1):
#         if listi[i] == "A":
#             listi[i] = "B"
#         else:
#             listi[i] = "A"

# count = 0
# # athuga hvort þurfi að swappa
# curr = n - 1
# while curr > 0:

#     if dna[curr] == "A":
#         dna[curr] = "B"
#         count = count + 1
#         curr = curr -1
#         continue
#     elif dna[curr-1] != "A":
#         swap(dna, curr)
#         print("var ad swappa, dna:",dna)
#         count = count + 1
#         curr = curr - 1
#     else:
#         curr = curr - 1
#         continue
# #flippa stökum elementum
# curr = n - 1
# while curr >= 0:
#     if dna[curr] == "A":
#         curr = curr - 1
#         continue
#     else:
#         dna[curr] = "A"
#         count = count + 1
#         curr = curr - 1

# print(count)







#test cases:
# 4 ABBA = 2
# 5 BBABB = 2
# 12 AAABBBAAABBB = 4
# 4 ABAB = 3