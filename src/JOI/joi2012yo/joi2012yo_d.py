N, K = map(int, input().split())
DP = [[[0 for _ in range(3)]for _ in range(2)]for _ in range(N)]
# [n日目][n日連続][nパスタ]
yote = [-1 for _ in range(N)]
for _ in range(K):
    d, p = map(int, input().split())
    yote[d - 1] = p - 1
if yote[0] != -1:
    DP[0][0][yote[0]] = 1
else:
    DP[0][0][1] = 1
    DP[0][0][2] = 1
    DP[0][0][0] = 1
for i in range(N - 1):
    if yote[i + 1] == -1 or yote[i + 1] == 0:
        DP[i + 1][0][0] = DP[i][0][1] + DP[i][0][2] + DP[i][1][1] + DP[i][1][2]
        DP[i + 1][1][0] = DP[i][0][0]
    if yote[i + 1] == -1 or yote[i + 1] == 1:
        DP[i + 1][0][1] = DP[i][0][0] + DP[i][0][2] + DP[i][1][0] + DP[i][1][2]
        DP[i + 1][1][1] = DP[i][0][1]
    if yote[i + 1] == -1 or yote[i + 1] == 2:
        DP[i + 1][0][2] = DP[i][0][1] + DP[i][0][0] + DP[i][1][1] + DP[i][1][0]
        DP[i + 1][1][2] = DP[i][0][2]
    for i in range(3):
        for j in range(2):
            DP[N - 1][j][i] %= 10000
ans = 0
for i in range(3):
    for j in range(2):
        ans += DP[N - 1][j][i]
print(ans % 10000)
