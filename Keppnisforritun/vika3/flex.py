data = input().split()
width = int(data[0])
nPartitions = int(data[1])
partitions = input().split()
partitionsSet = {width}
index = 0
curr = 0
while index < nPartitions:
    partitions[index] = int(partitions[index])
    partitionsSet.add(partitions[index])
    curr = abs(partitions[index] - width)
    if curr not in partitionsSet:
        partitionsSet.add(curr)
    for x in partitions:
        x = int(x)
        if x == partitions[index]:
            continue
        curr = abs(x - partitions[index])
        if curr not in partitionsSet:
            partitionsSet.add(curr)

    index = index + 1

utkoma = []
for x in partitionsSet:
    utkoma.append(x)
utkoma.sort()
        
print(*utkoma)

