H, W = map(int, input().split(" "))

maps = []
maps_ans = [[0] * W for i in range(H)]
maps_right = [[0] * W for i in range(H)]
maps_down = [[0] * W for i in range(H)]
maps_rd = [[0] * W for i in range(H)]
maps_ans[0][0] = 1
for i in range(H):
    maps.append(list(input()))

for i in range(H + W):
    for j in range(i + 1):
        if j < H and (i - j) < W:
            l = (i - j)
            if l + 1 < W and maps[j][l + 1] != "#":
                maps_ans[j][l + 1] += maps_ans[j][l] + maps_right[j][l]
                maps_right[j][l + 1] += maps_ans[j][l] + maps_right[j][l]
                maps_ans[j][l + 1] %= 10 ** 9 + 7
                maps_right[j][l + 1] %= 10 ** 9 + 7
            if j + 1 < H and maps[j + 1][l] != "#":
                maps_ans[j + 1][l] += maps_ans[j][l] + maps_down[j][l]
                maps_down[j + 1][l] += maps_ans[j][l] + maps_down[j][l]
                maps_ans[j + 1][l] %= 10 ** 9 + 7
                maps_down[j + 1][l] %= 10 ** 9 + 7
            if j + 1 < H and l + 1 < W and maps[j + 1][l + 1] != "#":
                maps_ans[j + 1][l + 1] += maps_ans[j][l] + maps_rd[j][l]
                maps_rd[j + 1][l + 1] += maps_ans[j][l] + maps_rd[j][l]
                maps_ans[j + 1][l + 1] %= 10 ** 9 + 7
                maps_rd[j + 1][l + 1] %= 10 ** 9 + 7
print(maps_ans[H - 1][W - 1])
