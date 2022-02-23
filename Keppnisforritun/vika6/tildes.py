data = input().split()
n = int(data[0]); q = int(data[1])

#hopar = [i for i in range(n)]
#staerdir = [1]*(n+1)
#print(staerdir)

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


unFind = UnionFind(n+1)
for i in range(q):
    data = input().split()
    fyrri = int(data[1])
    if data[0] == "t":
        seinni = int(data[2])
        unFind.union(fyrri, seinni)
    else:
        print(unFind.findSize(unFind.find(fyrri)))







