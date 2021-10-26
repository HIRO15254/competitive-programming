from collections import deque
N, u, v = map(int, input().split(" "))
rt = [[] for _ in range(N)]
leaf = []
for i in range(N - 1):
    A, B = map(int, input().split(" "))
    rt[A - 1].append(B - 1)
    rt[B - 1].append(A - 1)


def bfs(x):
    dis = [0] * N
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in rt[now]:
            if dis[i] == 0:
                q.append(i)
                dis[i] = dis[now] + 1
    dis[x] = 0
    return dis


dis_t = bfs(u - 1)
dis_a = bfs(v - 1)
ans = 0
for i in range(N):
    if dis_t[i] < dis_a[i]:
        ans = max(ans, dis_a[i] - 1)
print(ans)
