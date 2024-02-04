from collections import deque
INF = 10 ** 18
N, K = map(int, input().split())


def bfs(graph, x, INF=-1):
    dis = [INF] * N
    dis[x] = 0
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == INF:
                q.append(i)
                dis[i] = dis[now] + 1
    return dis


graph = [[] for _ in range(N)]
for i in range(N):
    inp = list(map(int, input().split()))
    for j in range(N):
        if inp[j] == 1:
            graph[i].append(j)

dists = []
for i in range(N):
    dists.append(bfs(graph, i, INF))

Q = int(input())
for i in range(Q):
    s, t = map(int, input().split())
    s_mod, t_mod = (s - 1) % N, (t - 1) % N
    if s_mod == t_mod:
        if t_mod not in graph[s_mod]:
            mi = INF
            for j in range(N):
                if j != s_mod:
                    mi = min(mi, dists[s_mod][j] + dists[j][t_mod])
            if mi == INF:
                print(-1)
            else:
                print(mi)
        else:
            print(1)
    else:
        if dists[s_mod][t_mod] == INF:
            print(-1)
        else:
            print(dists[s_mod][t_mod])
