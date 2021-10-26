H, W, N, M = map(int, input().split(" "))
maps = [["."] * W for i in range(H)]
light = [["."] * W for i in range(H)]
for _ in range(N):
    A, B = map(int, input().split(" "))
    maps[A - 1][B - 1] = "*"
for _ in range(M):
    A, B = map(int, input().split(" "))
    maps[A - 1][B - 1] = "#"

for i in range(H):
    st = 0
    lig = False
    for j in range(W):
        if maps[i][j] == "*":
            lig = True
        elif maps[i][j] == "#":
            if lig:
                for k in range(st, j):
                    light[i][k] = "*"
            st = j + 1
            lig = False
    if lig:
        for k in range(st, j + 1):
            light[i][k] = "*"


for j in range(W):
    st = 0
    lig = False
    for i in range(H):
        if maps[i][j] == "*":
            lig = True
        elif maps[i][j] == "#":
            if lig:
                for k in range(st, i):
                    light[k][j] = "*"
            st = i + 1
            lig = False
    if lig:
        for k in range(st, i + 1):
            light[k][j] = "*"

ans = 0
for i in range(H):
    ans += light[i].count("*")
print(ans)
