class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]



N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
tr = []
for i in range(N):
    tr.append([X[i], [i, -1], 1])
for i in range(N):
    tr.append([Y[i], [i, -1], 2])
for _ in range(M):
    A, B, Z = map(int, input().split())
    tr.append([Z, [A - 1, B - 1], 4])
tr.sort()

ans = 10 ** 18
for typ in range(1, 8):
    ans_now = 0
    uf = UnionFind(N)
    x_0, y_0 = -1, -1
    for i in tr:
        if typ & i[2]:
            if i[2] == 1:
                if x_0 == -1:
                    ans_now += i[0]
                    x_0 = i[1][0]
                    # print("x_0", x_0, i[0])
                elif not uf.issame(i[1][0], x_0):
                    uf.unite(i[1][0], x_0)
                    ans_now += i[0]
                    # print("x", i[1][0], i[0])
            if i[2] == 2:
                if y_0 == -1:
                    ans_now += i[0]
                    y_0 = i[1][0]
                    # print("y_0", y_0, i[0])
                elif not uf.issame(i[1][0], y_0):
                    uf.unite(i[1][0], x_0)
                    ans_now += i[0]
                    # print("y", i[1][0], i[0])
            if i[2] == 4:
                if not uf.issame(i[1][0], i[1][1]):
                    uf.unite(i[1][0], i[1][1])
                    ans_now += i[0]
                    # print("z", i[1][0], i[1][1], i[0])
    # print(typ, ans_now)
    if uf.size(0) == N:
        ans = min(ans, ans_now)
print(ans)