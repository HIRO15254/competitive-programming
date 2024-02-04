H, W = map(int, input().split(" "))
mapl = []
G = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    mapl.append(list(map(lambda x: 1 if x == "+" else -1, list(input()))))
turn = 1 if (H + W) % 2 == 1 else -1
for i in range(H + W - 2, -1, -1):
    for h in range(i + 1):
        w = i - h
        if h < H and w < W:
            if turn == -1:
                if h == H - 1:
                    G[h][w] = G[h][w + 1] - mapl[h][w]
                elif w == W - 1:
                    G[h][w] = G[h + 1][w] - mapl[h][w]
                else:
                    G[h][w] = max(G[h + 1][w], G[h][w + 1]) - mapl[h][w]
            else:
                if h == H - 1:
                    G[h][w] = G[h][w + 1] + mapl[h][w]
                elif w == W - 1:
                    G[h][w] = G[h + 1][w] + mapl[h][w]
                else:
                    G[h][w] = min(G[h + 1][w], G[h][w + 1]) + mapl[h][w]
    turn *= -1
G[0][0] += mapl[0][0] * turn
if G[0][0] > 0:
    print("Takahashi")
elif G[0][0] < 0:
    print("Aoki")
else:
    print("Draw")
