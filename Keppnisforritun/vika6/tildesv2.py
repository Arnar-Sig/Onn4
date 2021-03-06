
import sys
data = sys.stdin.readline().split()



# data = input().split()
n = int(data[0]); q = int(data[1])
items = [i for i in range(n)]
sizes = [1] * n

def union(p, q):
    if p == q:
        return
    p_root = root(p)
    q_root = root(q)
    if p_root == q_root:
        return

    if sizes[p_root] < sizes[q_root]:
        items[p_root] = q_root
        sizes[q_root] += sizes[p_root]
    else:
        items[q_root] = p_root
        sizes[p_root] += sizes[q_root]
def root(p):
    root = items[p]
    while not root == items[root]:
        items[root] = items[items[root]]
        root = items[root]
    items[p] = root
    return root

# def find(p):
#     return root(p)
# def findSize(x):
#     return sizes[x]


for i in range(q):
    data = sys.stdin.readline().split()
    fyrri = int(data[1]) - 1
    if data[0] == "t":
        seinni = int(data[2]) - 1
        union(fyrri, seinni)
    else:
        print(sizes[root(fyrri)])







