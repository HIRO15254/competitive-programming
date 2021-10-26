N = int(input())
A = list(map(int, input().split(" ")))
OR = [[-1] * N for _ in range(N)]
for i in range(N):
    que = 0
    for j in range(N - i):
        que = que | A[i + j]
        OR[i][i + j] = que
DP = [set() for _ in range(N + 1)]  # i個目まで計算済みのXOR
DP[0].add(0)
for i in range(N):
    for j in DP[i]:
        for k in range(N - i):
            DP[i + 1 + k].add(j ^ OR[i][i + k])
print(min(DP[N]))
