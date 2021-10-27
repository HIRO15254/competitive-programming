from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N, P = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))

ae = [0, 0]
ans = 0

for i in range(N):
    ae[A[i] % 2] += 1
for i in range(1, ae[1] + 1, 2):
    ans += cmb(ae[1], i)
ans *= 2 ** ae[0]

if P == 1:
    print(ans)
else:
    print(2 ** N - ans)
