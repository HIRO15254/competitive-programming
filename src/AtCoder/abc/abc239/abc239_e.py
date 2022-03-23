import sys
sys.setrecursionlimit(100000)

N, Q = map(int, input().split())
X = list(map(int, input().split()))
rank = [[-1 for _ in range(20)] for _ in range(N)]
edge = [[] for _ in range(N)]

def bfs(x, p = -1):
    ans = [X[x]]
    for i in edge[x]:
        if i != p:
            ans += bfs(i, x)
    ans.sort(reverse=True)
    rank[x] = ans[:21]
    return ans[:21]

for i in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    edge[A].append(B)
    edge[B].append(A)
bfs(0)
for i in range(Q):
    V, K = map(int, input().split())
    print(rank[V - 1][K - 1])