from functools import cmp_to_key


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
        self.tree[k] = min(self.tree[k], x)
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



def cmp(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    elif a[2] < b[2]:
        return 1
    elif a[2] > b[2]:
        return -1
    elif a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return 0


N = int(input())
box = []
min_x = set()
for i in range(N):
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    box.append(l)
    min_x.add(l[2])

min_x = list(min_x)
min_x.sort()
dic = {}
for i in range(len(min_x)):
    dic[min_x[i]] = i
for i in range(N):
    box[i][2] = dic[box[i][2]]
box.sort(key=cmp_to_key(cmp))

seg = SegTree([10 ** 18] * len(min_x), min, 10 ** 18)

ans = False
for i in range(N):
    seg.update(box[i][2], box[i][1])
    if seg.query(0, box[i][2]) < box[i][1]:
        ans = True
        break
if ans:
    print("Yes")
else:
    print("No")
