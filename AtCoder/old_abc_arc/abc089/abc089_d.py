H, W, D = map(int, input().split(" "))
mass = [[0 for _ in range(W)] for _ in range(H)]
num = [[0, 0] for _ in range(H * W + 1)]
DP = [0 for _ in range(H * W + 1)]
for i in range(H):
    mass[i] = list(map(int, input().split(" ")))
for i in range(H):
    for i2 in range(W):
        num[mass[i][i2]] = [i, i2]
for i in range(D, W * H + 1):
    DP[i] = DP[i - D] + abs(num[i][0] - num[i - D][0]) + abs(num[i][1] - num[i - D][1])
L = 0
R = 0
ans = 0
Q = int(input())
for i in range(Q):
    ans = 0
    L, R = map(int, input().split(" "))
    print(DP[R] - DP[L])
