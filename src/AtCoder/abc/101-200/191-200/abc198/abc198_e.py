import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
C = list(map(int, input().split(" ")))
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split(" "))
    edge[A - 1].append(B - 1)
    edge[B - 1].append(A - 1)
check = [-1] * N


def dfs(x, s):
    if not C[x] in s:
        s.add(C[x])
        check[x] = 1
    else:
        check[x] = 0

    p = []
    for i in edge[x]:
        if check[i] == -1:
            p.append(i)

    for i in p:
        if i == p[-1]:
            dfs(i, s)
        else:
            dfs(i, s.copy())


s = set()
dfs(0, s)
for i in range(N):
    if check[i] == 1:
        print(i + 1)
