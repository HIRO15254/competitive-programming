N, M = map(int, input().split())


def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][k] != INF and d[k][j] != INF:
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


INF = 10 ** 18

graph = [[INF for _ in range(N)] for _ in range(N)]

for i in range(M):
    u, v, c = map(int, input().split())
    graph[u - 1][v - 1] = c
for i in range(N):
    graph[i][i] = 0

graph = warshall_floyd(graph)

dp = [[INF for _ in range(1 << N)] for _ in range(N)]
for i in range(N):
    dp[i][1 << i] = 0

li = [[] for _ in range(N)]
for i in range(1, 1 << N):
    c = 0
    for j in range(N):
        if i & (1 << j):
            c += 1
    li[c - 1].append(i)

for k in range(N - 1):
    for p in li[k]:
        for now in range(N):
            if dp[now][p] == INF:
                continue
            for i in range(N):
                if graph[now][i] == INF:
                    continue
                if p & (1 << i) == 0:
                    dp[i][p | (1 << i)] = min(
                        dp[i][p | (1 << i)],
                        dp[now][p] + graph[now][i]
                    )

ans = INF
for i in range(N):
    ans = min(ans, dp[i][(1 << N) - 1])

if ans == INF:
    print("No")
else:
    print(ans)
