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
        return {r: self.members(r) for r in self.roots()}

    def all_sizes(self):
        """全連結成分のサイズのリストを取得 O(N)"""
        sizes = []
        for i in range(self.n):
            size = self.parents[i]
            if size < 0:
                sizes.append(-size)
        return sizes


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
card = []
uf = UnionFind(N)
for i in range(N):
    card.append([P[i], Q[i]])
card.sort()
for i in range(N):
    uf.union(i, card[i][1] - 1)
k = uf.all_sizes()
ans = 1
f = [1, 3]
for j in range(max(k)):
    f.append((f[-1] + f[-2]) % 998244353)
for i in k:
    ans *= f[i - 1]
    ans %= 998244353
print(ans)
