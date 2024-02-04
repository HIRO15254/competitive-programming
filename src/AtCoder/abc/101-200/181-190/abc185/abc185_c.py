L = int(input())
DP = [[0] * 12 for i in range(L)]
DP[0][0] += 1
for i in range(L - 1):
    for j in range(12):
        if j != 11:
            DP[i + 1][j + 1] += DP[i][j]
        DP[i + 1][j] += DP[i][j]
print(DP[L - 1][11])
