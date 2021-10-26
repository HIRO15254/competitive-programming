N = int(input())
DP = [1 for i in range(N + 60)]
for i in range(1, N + 1):
    D_S = 0
    for j in range(7):
        D_S += i % 10 ** (j + 1) // 10 ** j
    DP[i + D_S] += DP[i]
print(DP[N])
