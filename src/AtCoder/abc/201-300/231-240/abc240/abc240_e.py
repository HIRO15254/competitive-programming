import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
edge = [[] for _ in range(N)]
ans = dict()
now = 1
for i in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().rstrip().split())
    edge[A].append(B)
    edge[B].append(A)

def bfs(x, p = -1):
    global now, ans
    _ans = [now, now]
    for i in edge[x]:
        if i != p:
            k = bfs(i, x)
            if k[0] < _ans[0] or _ans[0] == now:
                _ans[0] = k[0]
            if k[1] > _ans[1] or _ans[0] == now:
                _ans[1] = k[1]
    if _ans[0] == now:
        now += 1
    ans[x] = _ans
    return _ans

bfs(0)
for i in range(N):
    print(ans[i][0], ans[i][1])