N, M = map(int, input().split(" "))
MASS = [[] for _ in range(11)]
for i in range(N):
    S = input()
    for j in range(M):
        if S[j] == "S":
            MASS[0].append([j, i])
        elif S[j] == "G":
            MASS[10].append([j, i])
        else:
            MASS[int(S[j])].append([j, i])
INF = 10 ** 18
dp = [[INF for _ in range(len(MASS[i]))]for i in range(11)]
dp[0][0] = 0
for i in range(10):
    for j in range(len(MASS[i])):
        for k in range(len(MASS[i + 1])):
            dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + abs(MASS[i][j][0] - MASS[i + 1][k][0]) + abs(MASS[i][j][1] - MASS[i + 1][k][1]))
if (dp[10][0] < INF):
    print(dp[10][0])
else:
    print(-1)
