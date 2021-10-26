N = int(input())
S = list(input())
S = S
J = [0, 1, 0, 1, 0, 1, 0, 1]
O = [0, 0, 1, 1, 0, 0, 1, 1]
I = [0, 0, 0, 0, 1, 1, 1, 1]
DP = [[0] * 8 for _ in range(N + 1)]
DP[0][1] = 1
for i in range(N):
    for j in range(8):
        if S[i] == "J":
            if J[j] == 1:
                DP[i + 1][1] += DP[i][j]
                DP[i + 1][3] += DP[i][j]
                DP[i + 1][5] += DP[i][j]
            elif j == 2:
                DP[i + 1][3] += DP[i][j]
            elif j == 4:
                DP[i + 1][5] += DP[i][j]
            elif j == 6:
                DP[i + 1][5] += DP[i][j]
                DP[i + 1][3] += DP[i][j]
        if S[i] == "O":
            if O[j] == 1:
                DP[i + 1][2] += DP[i][j]
                DP[i + 1][3] += DP[i][j]
                DP[i + 1][6] += DP[i][j]
            elif j == 1:
                DP[i + 1][3] += DP[i][j]
            elif j == 4:
                DP[i + 1][6] += DP[i][j]
            elif j == 5:
                DP[i + 1][3] += DP[i][j]
                DP[i + 1][6] += DP[i][j]
        if S[i] == "I":
            if I[j] == 1:
                DP[i + 1][4] += DP[i][j]
                DP[i + 1][5] += DP[i][j]
                DP[i + 1][6] += DP[i][j]
            elif j == 1:
                DP[i + 1][5] += DP[i][j]
            elif j == 2:
                DP[i + 1][6] += DP[i][j]
            elif j == 3:
                DP[i + 1][5] += DP[i][j]
                DP[i + 1][6] += DP[i][j]
        DP[i + 1][7] += DP[i][j]
    for j in range(8):
        DP[i + 1][j] %= 10007
print(sum(DP[N]) % 10007)
