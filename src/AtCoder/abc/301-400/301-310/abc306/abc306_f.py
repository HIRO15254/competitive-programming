import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
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
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
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


N, M = map(int, input().split())
zaatu = []
for i in range(N):
    lis = list(map(int, input().split()))
    for j in lis:
        zaatu.append([j, i])
zaatu.sort()
new_A = [[] for _ in range(N)]
for i in range(N * M):
    new_A[zaatu[i][1]].append(i)

seg = SegTree([0] * (N * M), lambda x, y: x + y, 0)
ans = 0

for i in range(N):
    for j in range(M):
        i2 = N - 1 - i
        ans += i * (j + 1) + seg.query(0, new_A[i2][j])
    for j in range(M):
        seg.update(new_A[i2][j], 1)
print(ans)
