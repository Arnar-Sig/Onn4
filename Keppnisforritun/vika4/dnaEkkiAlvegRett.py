# breytur etc
n = int(input())
data = input()
dna = [i for i in data]
a = 0
b = 0
bBefore= []

### swap fallið ###
def swap(listi, percentages, k):
    # print("Kallað á swap með k:", k)
    # print("listi fyrir:", dna)
    # print("percentages fyrir:", bBefore)
    for i in range(k + 1):
        if listi[i] == "A":
            listi[i] = "B"
        else:
            listi[i] = "A"
        percentages[i] = 1 - percentages[i]
    # print("listi eftir:", dna)
    # print("percentages eftir:", bBefore)

### finna hversu mörg B eru fyrir framan hvert stak ###
# fyrsta stakið
if dna[0] == "A":
    a = a + 1
    bBefore.append(0)
else:
    b = b + 1
    bBefore.append(100)
# restin af lista
for i in range(1,n):
    if dna[i] == "B":
        b = b + 1
    else:
        a = a + 1
    if a == 0:
        bBefore.append(100)
    else:
        bBefore.append(b/(a + b))

count = 0


# athuga hvort þurfi að swappa
curr = n - 1
while curr > 0:

    if bBefore[curr] < 0.5 or dna[curr] == "A" or (dna[curr] != dna[curr-1]):
        curr = curr -1
        continue
    else:
        swap(dna, bBefore, curr)
        count = count +1
        curr = curr -1

#print("count og listi eftir swapperinn:", count, dna)

#flippa stökum elementum
curr = n - 1
while curr >= 0:
    if dna[curr] == "A":
        curr = curr - 1
        continue
    else:
        dna[curr] = "A"
        count = count + 1
        curr = curr - 1
print(count)
    
