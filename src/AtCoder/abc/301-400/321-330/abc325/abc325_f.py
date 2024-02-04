N = int(input())
D = list(map(int, input().split()))
L_1, C_1, K_1 = map(int, input().split())
L_2, C_2, K_2 = map(int, input().split())

dp = [[10 ** 20 for _ in range(K_1 + 1)] for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N):
    for s_1 in range(((D[i] - 1) // L_1) + 2):
        s_2 = max(0, ((D[i] - s_1 * L_1) - 1) // L_2 + 1)
        # print(D[i], s_1, s_2)
        for j in range(K_1 - s_1 + 1):
            if dp[i][j] != -1:
                dp[i + 1][j + s_1] = min(dp[i + 1][j + s_1], dp[i][j] + s_2)
ans = 10 ** 20
for i in range(K_1 + 1):
    if dp[N][i] <= K_2:
        ans = min(ans, C_1 * i + C_2 * dp[N][i])
        # print(i, dp[N][i], ans)
if ans == 10 ** 20:
    print(-1)
else:
    print(ans)
