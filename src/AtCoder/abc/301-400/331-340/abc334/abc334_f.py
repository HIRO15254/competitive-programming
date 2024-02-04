class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = self.segfunc(self.tree[k], x)
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

N, K = map(int, input().split())

S_x, S_y = map(int, input().split())
INF = 10 ** 18


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def s_dist(x1, y1, x2, y2):
    dist_1 = dist(x1, y1, S_x, S_y)
    dist_2 = dist(x2, y2, S_x, S_y)
    return dist_1 + dist_2 - dist(x1, y1, x2, y2)


seg = SegTree([0] * K + [INF] * (N + 1), min, INF)

min_dist = 0
last_x, last_y = S_x, S_y
for i in range(N):
    x, y = map(int, input().split())
    min_dist += dist(last_x, last_y, x, y)
    t = i + K
    seg.update(t, seg.query(i, t) + s_dist(x, y, last_x, last_y))
    last_x, last_y = x, y

print(seg.query(N, N + K) + min_dist + dist(last_x, last_y, S_x, S_y))
