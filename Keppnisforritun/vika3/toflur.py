
n = int(input())
data = input().split()
mengi = set()
for x in data:
   mengi.add(int(x))
#print(mengi)
eftirMengi = []
for x in mengi:
    eftirMengi.append(x)
eftirMengi.sort()
sum = 0
i = 1
while i < len(eftirMengi):
    sum = sum + pow((eftirMengi[i-1] - eftirMengi[i]), 2)
    i = i + 1
print(sum)