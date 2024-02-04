N, K = map(int, input().split())
A = list(map(int, input().split())) + [10 ** 18 + 1]
s = []
k = 0
for i in range(N):
    if A[k] == i + 1:
        s.append(i)
        k += 1
    else:
        s.append(i)
        s.append(i)
for i in range(10):
    s.append(10 ** 18 + 1)

INF = 10 ** 18
DP = [[INF] * 2 for _ in range(len(s))]
DP[0][0] = 0
for i in range(N * 2 - K):
    if DP[i][0] != INF:
        DP[i + 2][0] = min(DP[i + 2][0], DP[i][0] + s[i + 1] - s[i])
        DP[i + 3][1] = min(DP[i + 2][1], DP[i][0] + s[i + 2] - s[i + 1])
    if DP[i][1] != INF:
        DP[i + 2][1] = min(DP[i + 2][1], DP[i][1] + s[i + 1] - s[i])
print(DP[N * 2 - K][K % 2])
