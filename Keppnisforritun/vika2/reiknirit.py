from collections import Counter

n = int(input())
data = input().split()
mengi = Counter(data)# óbreytt inntak talið
utkoma = 0
vals = mengi.values()
listi = []
for x in vals:
    listi.append(x)

listi.sort(reverse=True)
ut = n
curr = n
for x in listi:
    ut = ut + (curr - x)
    curr = curr - x
print(ut)

