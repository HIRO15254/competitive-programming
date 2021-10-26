W, H = map(int, input().split(" "))
DP = [[[0] * 3 for _ in range(H + 2)]for _ in range(W + 2)]
DP[1][0][0] = 1
DP[0][1][1] = 1
for i in range(1, W + H + 1):
    for w in range(i + 1):
        h = i - w
        if 0 <= w and w < W and 0 <= h and h < H:
            DP[w][h][0] %= 100000
            DP[w][h][1] %= 100000
            DP[w + 1][h][0] += DP[w][h][0]
            DP[w][h + 2][1] += DP[w][h][0]
            DP[w][h + 1][2] += DP[w][h][0]
            DP[w][h + 1][1] += DP[w][h][1]
            DP[w + 2][h][0] += DP[w][h][1]
            DP[w + 1][h][2] += DP[w][h][1]
print(sum(DP[W - 1][H - 1]) % 100000)
