import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10 ** 6)


N, X, Y = map(int, input().split())
edge = [[] for _ in range(N)]


def solve(n, p):
    if (n == X - 1):
        return [X]
    for i in edge[n]:
        if (i != p):
            s = solve(i, n)
            if s != []:
                return s + [n + 1]
    return []


for _ in range(N - 1):
    A, B = map(int, input().split())
    edge[A - 1].append(B - 1)
    edge[B - 1].append(A - 1)
print(" ".join(map(str, solve(Y - 1, -1))))
