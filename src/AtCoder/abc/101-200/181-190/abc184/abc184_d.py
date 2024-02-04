A, B, C = map(int, input().split(" "))
DP = [[[0] * 101 for i in range(101)]for _ in range(101)]

DP[A][B][C] = 1

for i in range(1, 301):
    for a in range(i + 1):
        for b in range(i - a + 1):
            c = i - a - b
            if max(a, b, c) < 100:
                DP[a + 1][b][c] += DP[a][b][c] * a / (a + b + c)
                DP[a][b + 1][c] += DP[a][b][c] * b / (a + b + c)
                DP[a][b][c + 1] += DP[a][b][c] * c / (a + b + c)


ans = 0
for b in range(100):
    for c in range(100):
        ans += DP[100][b][c] * (100 - A + b - B + c - C)
for a in range(100):
    for c in range(100):
        ans += DP[a][100][c] * (a - A + 100 - B + c - C)
for b in range(100):
    for a in range(100):
        ans += DP[a][b][100] * (a - A + b - B + 100 - C)

print(ans)
