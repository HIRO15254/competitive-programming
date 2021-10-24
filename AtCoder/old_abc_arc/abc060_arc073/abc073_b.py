N, W = map(int, input().rstrip().split(" "))
DP = [[-1 for _ in range(310)] for _ in range(N + 1)]
DP[0][0] = 0
ans = 0
for i in range(N):
    w, v = map(int, input().rstrip().split(" "))
    if i == 0:
        w1 = w
    for i2 in range(i, -1, -1):
        for i3 in range(309, -1, -1):
            if DP[i2][i3] != -1:
                DP[i2 + 1][i3 + (w - w1)] = max(DP[i2 + 1][i3 + (w - w1)], DP[i2][i3] + v)
                if i2 * w1 + i3 + w <= W:
                    ans = max(DP[i2 + 1][i3 + (w - w1)], ans)
print(ans)
