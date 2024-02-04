N = int(input())
dp = [[0, 0] for _ in range(N + 1)]
for i in range(N):
    X, Y = map(int, input().split())
    if X == 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][0] + Y, dp[i][1] + Y)
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + Y)
print(max(dp[N]))
