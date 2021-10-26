N, K = map(int, input().split(" "))
ku = []
dp = [0 for i in range(N)]
dp[0] = 1
dp[1] = -1
for _ in range(K):
    L, R = map(int, input().split(" "))
    ku.append([L, R + 1])
for i in range(N):
    if i > 0:
        dp[i] += dp[i - 1]
    dp[i] %= 998244353
    for j in range(K):
        l, r = ku[j]
        if (i + l < N):
            dp[i + l] += dp[i]
        if (i + r < N):
            dp[i + r] -= dp[i]
print(dp[N - 1])
