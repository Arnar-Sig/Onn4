import sys

data = sys.stdin.readline().split()
fjoldi = int(data[0]); experiments = int(data[1])
adj = [set() for i in range(0, fjoldi)]
source = [1]*fjoldi
for i in range(experiments):
    data = sys.stdin.readline().split()
    eitt = int(data[0]); tvo = int(data[1])
    adj[eitt].add(tvo)
    source[tvo] = 0

byrjun = []
finish = 0
for i in range(len(adj)):
    if source[i] == 1:
        byrjun.append(i)
    if len(byrjun) > 1 or len(adj[i])>1:
        print("back to the lab")
        finish = 1
        break

# if len(byrjun) == 0:
#     print("back to the lab")
#     finish = 1

#print("adj:", adj)

if finish == 0:
    utkoma = []
    curr = byrjun[0]
    for i in range(fjoldi):
        if len(adj[curr]) ==0:
            utkoma.append(curr)
            break
        utkoma.append(curr)
        curr = adj[i].pop()
        
    strengur = ' '.join(str(e) for e in utkoma)
    print(strengur)

