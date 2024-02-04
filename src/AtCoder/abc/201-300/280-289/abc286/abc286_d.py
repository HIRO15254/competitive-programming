N, X = map(int, input().split())
DP = [[False for _ in range(X + 1)] for _ in range(N + 1)]
DP[0][0] = True
for i in range(N):
    A, B = map(int, input().split())
    for j in range(A):
        counter = 0
        k = 0
        while j + k * A <= X:
            if DP[i][j + k * A]:
                counter += 1
            if k >= (B + 1) and DP[i][j + (k - B - 1) * A]:
                counter -= 1
            if counter > 0:
                DP[i + 1][j + k * A] = True
            k += 1
print("Yes" if DP[-1][-1] else "No")
