N, M = map(int, input().split(" "))
DP = [[10 ** 18] * (N + 1) for _ in range(M + 1)]
DP[0][0] = 0
D = []
C = []
for i in range(N):
    D.append(int(input()))
for i in range(M):
    C.append(int(input()))

for i in range(M):
    for j in range(N):
        DP[i + 1][j] = min(DP[i + 1][j], DP[i][j])
        DP[i + 1][j + 1] = min(DP[i + 1][j + 1], DP[i][j] + D[j] * C[i])
ans = 10 ** 18
for i in range(M + 1):
    ans = min(ans, DP[i][N], ans)
print(ans)
