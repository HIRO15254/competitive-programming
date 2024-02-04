N, M, K = map(int, input().split())
DP = [[0 for _ in range((N * M) + 2)] for _ in range(N + 1)]
DP[0][0] = 1
for i in range(N):
    for j in range(i * M + 1):
        for k in range(1, M + 1):
            DP[i + 1][j + k] += DP[i][j]
    for j in range(i * (M + 1)):
        DP[i + 1][j] %= 998244353
print(sum(DP[-1][:(K + 1)]) % 998244353)
