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


def main():
    from sys import stdin
    N, M = map(int, input().split(" "))
    uf = UnionFind(N)
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    for i in range(M):
        c, d = map(int, stdin.readline().split(" "))
        uf.union(c - 1, d - 1)

    ac = [0] * N
    bc = [0] * N
    for i in range(N):
        k = uf.find(i)
        ac[k] += a[i]
        bc[k] += b[i]
    if ac == bc:
        print("Yes")
    else:
        print("No")


main()
