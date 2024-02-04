H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(list(input()))
ans = True
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            if i - 1 >= 0 and grid[i - 1][j] == "#":
                continue
            if i + 1 < H and grid[i + 1][j] == "#":
                continue
            if j - 1 >= 0 and grid[i][j - 1] == "#":
                continue
            if j + 1 < W and grid[i][j + 1] == "#":
                continue
            ans = False
if ans:
    print("Yes")
else:
    print("No")
