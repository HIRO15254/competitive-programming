D, N = map(int, input().split(" "))
DP = [[-1] * 101 for _ in range(D)]
q = [[] for _ in range(61)]
T = []
C = []
for i in range(D):
    T.append(int(input()))
for i in range(N):
    a, b, c = map(int, input().split(" "))
    for i in range(a, b + 1):
        q[i].append(c)

for i in q[T[0]]:
    DP[0][i] = 0
for i in range(D - 1):
    for j in range(101):
        if DP[i][j] != -1:
            for k in q[T[i + 1]]:
                DP[i + 1][k] = max(DP[i + 1][k], DP[i][j] + abs(j - k))

print(max(DP[D - 1]))
