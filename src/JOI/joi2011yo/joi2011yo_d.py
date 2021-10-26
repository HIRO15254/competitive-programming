N = int(input())
DP = [[0 for _ in range(21)]for _ in range(N + 1)]
DP[0][0] = 1
A = list(map(int, input().split(" ")))
for i in range(N - 1):
    for j in range(21):
        if j + A[i] <= 20:
            DP[i + 1][j + A[i]] += DP[i][j]
        if j - A[i] >= 0:
            DP[i + 1][j - A[i]] += DP[i][j]
print(DP[N - 1][A[N - 1]])
