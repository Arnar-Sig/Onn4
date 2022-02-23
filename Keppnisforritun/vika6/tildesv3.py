data = input().split()
n = int(data[0]); q = int(data[1])
items = [i for i in range(n)]
sizes = [1] * n

def union(p, q):
    p_root = root(p)
    q_root = root(q)
    if sizes[p_root] < sizes[q_root]:
        items[p_root] = q_root
        sizes[q_root] += sizes[p_root]
    else:
        items[q_root] = p_root
        sizes[p_root] += sizes[q_root]
def root(p):
    while items[p] != p:
        items[p] = items[items[p]]
        p = items[p]
    items[p] = root
    return p

for i in range(q):
    data = input().split()
    fyrri = int(data[1]) - 1
    if data[0] == "t":
        seinni = int(data[2]) - 1
        union(fyrri, seinni)
    else:
        print(sizes[root(fyrri)])
