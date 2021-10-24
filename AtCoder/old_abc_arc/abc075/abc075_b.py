H, W = map(int, input().split(" "))
maps = [["."] * (W + 2)]
for i in range(H):
    maps.append(list("." + input() + "."))
maps.append(["."] * (W + 2))
ans = [[" "] * W for _ in range(H)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if maps[i][j] == "#":
            ans[i - 1][j - 1] = "#"
        else:
            c = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if maps[i + k][j + l] == "#":
                        c += 1
            ans[i - 1][j - 1] = str(c)
for i in range(H):
    print("".join(ans[i]))
