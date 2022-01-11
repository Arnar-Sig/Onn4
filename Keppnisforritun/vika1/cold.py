number = int(input())
data = input()

listi = data.split()
belowZero = 0
for x in listi:
    if int(x) < 0:
        belowZero = belowZero + 1
print(belowZero)
