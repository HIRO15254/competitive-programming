H, W = map(int, input().split(" "))
maps = []
ans = 0
for i in range(H):
    maps.append(input())
for i in range(1, H):
    for j in range(1, W):
        k = 0
        if maps[i - 1][j - 1] == "#":
            k += 1
        if maps[i - 1][j] == "#":
            k += 1
        if maps[i][j - 1] == "#":
            k += 1
        if maps[i][j] == "#":
            k += 1
        if k == 1 or k == 3:
            ans += 1
print(ans)
