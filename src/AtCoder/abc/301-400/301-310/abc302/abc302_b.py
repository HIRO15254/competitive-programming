H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            for ang_x in range(-1, 2):
                for ang_y in range(-1, 2):
                    if 0 <= i + ang_x * 4 and i + ang_x * 4 < H and 0 <= j + ang_y * 4 and j + ang_y * 4 < W:
                        if (S[i + ang_x][j + ang_y] == "n" and S[i + ang_x * 2][j + ang_y * 2] == "u" and S[i + ang_x * 3][j + ang_y * 3] == "k" and S[i + ang_x * 4][j + ang_y * 4] == "e"):
                            for k in range(5):
                                print(i + ang_x * k + 1, j + ang_y * k + 1)
                            exit()
