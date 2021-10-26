N = int(input())
DP = [[0] * 2 for _ in range(N + 1)]
DP[0] = [1, 1]
for i in range(N):
    S = input()
    if S == "OR":
        DP[i + 1][0] = DP[i][0] * 2 + DP[i][1]
        DP[i + 1][1] = DP[i][1]
    else:
        DP[i + 1][0] = DP[i][0]
        DP[i + 1][1] = DP[i][0] + DP[i][1] * 2
print(DP[N][0])
