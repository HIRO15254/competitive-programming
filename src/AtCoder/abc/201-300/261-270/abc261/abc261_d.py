N, M = map(int, input().split())
X = list(map(int, input().split()))
B = {}
for i in range(M):
    C, Y = map(int, input().split())
    B[C - 1] = Y
mon = [0]
now = 0
for i in range(N):
    if i in B:
        now += B[i]
    mon.append(now)
mon_2 = [0]
now = 0
for i in range(N):
    now += X[i]
    mon_2.append(now)

dp = [0] * (N + 1)
for i in range(N):
    for j in range(1, N - i + 1):
        dp[i + j] = max(dp[i + j], dp[i] + mon[j - 1] + mon_2[i + j - 1] - mon_2[i])
    dp[N] = max(dp[N], dp[i] +  mon[N - i] + mon_2[N] - mon_2[i])
print(dp[N])
