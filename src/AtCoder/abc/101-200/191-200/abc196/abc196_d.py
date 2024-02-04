H, W, A, B = map(int, input().split(" "))
# [A][B][bit]
DP = [[[0 for _ in range(2**(H * W))] for _ in range(B + 1)] for _ in range(A + 1)]
DP[0][0][0] = 1
for i in range(2**(H * W)):
    for j in range(H * W):
        if (not (i >> j) & 1):
            for a in range(A + 1):
                for b in range(B + 1):
                    if b != B:
                        DP[a][b + 1][i + 2**j] += DP[a][b][i]
                    if a != A:
                        if j % W != W - 1 and (not (i >> (j + 1)) & 1):
                            DP[a + 1][b][i + 2**j + 2**(j + 1)] += DP[a][b][i]
                        if j // W != H - 1 and (not (i >> (j + W)) & 1):
                            DP[a + 1][b][i + 2**j + 2**(j + W)] += DP[a][b][i]
            break
print(DP[A][B][2**(H * W) - 1])
