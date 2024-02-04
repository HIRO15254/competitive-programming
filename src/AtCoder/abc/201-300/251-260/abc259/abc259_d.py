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


def mag(x, y):
    return x * x + y * y


N = int(input())
sx, sy, tx, ty = map(int, input().split())
start, end = -1, -1
uf = UnionFind(N)
circles = []
for i in range(N):
    circles.append(list(map(int, input().split())))
for i in range(N):
    for j in range(i + 1, N):
        dist = mag(circles[i][0] - circles[j][0], circles[i][1] - circles[j][1])
        if (circles[i][2] - circles[j][2]) ** 2 <= dist and dist <= (circles[i][2] + circles[j][2]) ** 2:
            uf.union(i, j)
    if mag(circles[i][0] - sx, circles[i][1] - sy) == circles[i][2] ** 2:
        start = i
    if mag(circles[i][0] - tx, circles[i][1] - ty) == circles[i][2] ** 2:
        end = i
if uf.same(start, end):
    print("Yes")
else:
    print("No")
