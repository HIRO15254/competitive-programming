INF = 10 ** 18
N = int(input())
points = []
for i in range(N):
    x, y, z = map(int, input().split(" "))
    points.append([x, y, z])
dist = [[INF for i in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            dist[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i]
                                                                [1] - points[j][1]) + max(points[j][2] - points[i][2], 0)
dp = [[INF] * N for _ in range(2 ** N)]
dp[0][0] = 0
for k in range(2 ** N):
    for i in range(N):
        for j in range(N):
            dp[k | (1 << j)][j] = min(
                dp[k | (1 << j)][j], dp[k][i] + dist[i][j])
print(dp[2 ** N - 1][0])
