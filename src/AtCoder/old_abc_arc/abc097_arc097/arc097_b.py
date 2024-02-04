class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n)if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        groups = {r: set() for r in self.roots()}
        for i in range(self.n):
            groups[self.find(i)].add(i)
        return groups


N, M = map(int, input().split())
A = list(map(int, input().split()))
uf = UnionFind(N)
for _ in range(M):
    x, y = map(int, input().split())
    uf.union(x - 1, y - 1)
ans = 0
u = uf.all_group_members().values()
for i in u:
    for j in i:
        if(A[j] - 1 in i):
            ans += 1
print(ans)
