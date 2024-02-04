class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
        self.elc = [False] * n

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
        ret = 0
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return 0 # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.elc[ry] and not self.elc[rx]:
            ret = self.size(rx)
        elif not self.elc[ry] and self.elc[rx]:
            ret = self.size(ry)
        self.elc[ry] = self.elc[ry] or self.elc[rx]
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return ret

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

    # 特定のノードに電源を接続する
    def addElc(self, x):
        if not self.elc[self.root(x)]:
            self.elc[self.root(x)] = True
            return self.size(x)
        return 0

    def elcCount(self):
        ans = 0
        for i in range(len(self.elc)):
            if self.elc[self.root(i)]:
                ans += 1
        return ans




N, M, E = map(int, input().split())
uf = UnionFind(N)
edge = []
for _ in range(E):
    A, B = map(int, input().split())
    edge.append([A - 1, B - 1])
Q = int(input())
C = [True] * E
X = []
for _ in range(Q):
    X.append(int(input()) - 1)
    C[X[-1]] = False
X.reverse()
for i in range(E):
    if C[i]:
        if edge[i][0] < N:
            if edge[i][1] < N:
                uf.unite(edge[i][0], edge[i][1])
            else:
                uf.addElc(edge[i][0])
ans = [uf.elcCount()]
for i in X:
    if edge[i][0] < N:
        if edge[i][1] < N:
            ans.append(ans[-1] + uf.unite(edge[i][0], edge[i][1]))
        else:
            ans.append(ans[-1] + uf.addElc(edge[i][0]))
ans.reverse()
for i in range(Q):
    print(ans[1 + i])
