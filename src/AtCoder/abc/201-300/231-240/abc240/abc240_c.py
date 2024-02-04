N, X = map(int, input().split())
DP = [[False for _ in range(10001)] for _ in range(N + 1)]
DP[0][0] = True
for i in range(N):
    a, b = map(int, input().split())
    for j in range(10001):
        if DP[i][j]:
            if j + a <= 10000:
                DP[i + 1][j + a] = True
            if j + b <= 10000:
                DP[i + 1][j + b] = True
if DP[-1][X]:
    print("Yes")
else:
    print("No")
