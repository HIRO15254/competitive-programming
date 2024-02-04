from collections import deque

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

N, M = map(int, input().split())
D = list(map(int, input().split()))
ans = True
if sum(D) != (N * 2 - 2):
    ans = False
UF = UnionFind(N)
for i in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())
    UF.union(A, B)
    D[A] -= 1
    D[B] -= 1
ag = UF.all_group_members()
D2 = []
for i in ag:
    L = []
    for j in ag[i]:
        for k in range(D[j]):
            L.append(j)
    if len(L) == 0:
        ans = False
    D2.append([len(L), L])
D2.sort(reverse=True)
if not ans:
    print(-1)
else:
