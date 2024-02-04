N, M ,K, S, T ,X = map(int, input().split(" "))
hen = [[] for i in range(N)]
for i in range(M):
    U, V = map(int, input().split(" "))
    hen[U - 1].append(V - 1)
    hen[V - 1].append(U - 1)
SX = [0] * (K + 1)
XX = [0] * (K + 1)
XT = [0] * (K + 1)
# S -> T
ans = 0
DP = [[0 for _ in range(N)] for _ in range(K + 1)]
DP[0][S - 1] = 1
for i in range(K):
    for j in range(N):
        for k in hen[j]:
            if k != X - 1:
                DP[i + 1][k] += DP[i][j]
ans += DP[-1][T - 1]
# S -> X
DP = [[0 for _ in range(N)] for _ in range(K + 1)]
DP[0][S - 1] = 1
for i in range(K):
    for j in range(N):
        for k in hen[j]:
            DP[i + 1][k] += DP[i][j]
    SX[i + 1] = DP[i + 1][X - 1]
    DP[i + 1][X - 1] = 0
# X -> X
DP = [[0 for _ in range(N)] for _ in range(K + 1)]
DP[0][X - 1] = 1
for i in range(K):
    for j in range(N):
        for k in hen[j]:
            DP[i + 1][k] += DP[i][j]
    XX[i + 1] = DP[i + 1][X - 1]
    DP[i + 1][X - 1] = 0
# X -> T
DP = [[0 for _ in range(N)] for _ in range(K + 1)]
DP[0][X - 1] = 1
for i in range(K):
    for j in range(N):
        for k in hen[j]:
            DP[i + 1][k] += DP[i][j]
    XT[i + 1] = DP[i + 1][T - 1]
    DP[i + 1][T - 1] = 0
print(SX)
print(XX)
print(XT)
# S -> X -> X ( -> X -> X) 任意回 -> T
# X_DP[X自己ループ回数][総回数]
X_DP = [[0 for _ in range(K + 1)] for _ in range(K + 1)]
X_DP[0] = SX
end = [0] * (K + 1)
i = 0
while X_DP[i] != end:
    if i % 2 == 1:
        for j in range(K + 1):
            ans += X_DP[i][j] * XT[K - j]
    ans %= 998244353
    for j in range(K + 1):
        if X_DP[i][j] != 0:
            for k in range(K + 1 - j):
                X_DP[i + 1][j + k] += X_DP[i][j] * XX[k]
    i += 1
print(X_DP)
print(ans)