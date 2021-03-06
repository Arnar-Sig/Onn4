import sys

class UnionFind():
    def __init__(self, n):
        self.items = list(range(n))
        self.sizes = [1] * n
        self.count = len(self.items)

    def union(self, p, q):
        if p == q:
            return
        p_root = self._root(p)
        q_root = self._root(q)
        if p_root == q_root:
            return

        if self.sizes[p_root] < self.sizes[q_root]:
            self.items[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.items[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]
        self.count -= 1

    def _root(self, p):
        root = self.items[p]
        while not root == self.items[root]:
            self.items[root] = self.items[self.items[root]]
            root = self.items[root]
        self.items[p] = root
        return root

    def find(self, p):
        return self._root(p)

    def connected(self, p, q):
        return p == q or self.find(p) == self.find(q)

    def count(self):
        return self.count

    def findSize(self, x):
        return self.sizes[x]

while True:
    # Lesa inn fjölda hnúta og leggja
    data = sys.stdin.readline().split()
    nNodes = int(data[0]); nEdges = int(data[1])
    if nNodes == 0 and nEdges == 0:
        break

    # Búa til union find hlut til að athuga hvort hnútar séu tengdir 
    UF = UnionFind(nNodes)
    hnutar = []

    # Bæta við leggjum (og hnútunum sem tengjast leggnum) 
    # og raða eftir lengd (vaxandi)
    for i in range(nEdges):
        data = sys.stdin.readline().split()
        a = int(data[0]); b = int(data[1]); lengd = int(data[2])
        hnutar.append((lengd, a, b,))
    sorted_lengdir = sorted(hnutar, key=lambda x: x[0])

    # Bæta við hnútununm (tuple) sem tengja minnsta legginn ef hnútarnir
    # tilheyra ekki sama hóp
    mst = []
    cost = 0
    i = 0
    lengdMST = len(mst)
    lengdSortedLengdir = len(sorted_lengdir)
    while lengdMST < (nNodes-1) and i < lengdSortedLengdir:
        if not UF.connected(sorted_lengdir[i][1], sorted_lengdir[i][2]):
            mst.append((sorted_lengdir[i][1], sorted_lengdir[i][2]))
            UF.union(sorted_lengdir[i][1], sorted_lengdir[i][2])
            cost = cost + sorted_lengdir[i][0]
        i += 1
    
    # raða leggjunum í minnsta spanntrénu fyrst eftir fyrri hnút 
    # og annars seinni hnút, athuga svo hvort réttur fjöldi 
    # hnúta fyrir minnsta spanntré (V-1) og prenta útkomuna
    #sorted_hnutar = sorted(mst, key=lambda x: (x[0], x[1]))
    sorted_hnutar = []
    for i in range(len(mst)):
        sorted_hnutar.append(sorted(mst[i]))
    sorted_hnutar = sorted(sorted_hnutar, key=lambda x: (x[0], x[1]))

    if len(mst) == (nNodes-1):
        print(cost)
        for j in range(len(sorted_hnutar)):
            print(*sorted_hnutar[j])
    else:
        print("Impossible")




