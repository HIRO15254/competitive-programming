H, W, X, Y = map(int, input().split(" "))
maps = []
maps.append(["#"] * (W + 2))
for i in range(H):
    maps.append(list("#" + input() + "#"))
maps.append(["#"] * (W + 2))
ans = -3
for i in range(H + 2):
    if maps[X + i][Y] == "#":
        break
    else:
        ans += 1
for i in range(H + 2):
    if maps[X - i][Y] == "#":
        break
    else:
        ans += 1
for i in range(W + 2):
    if maps[X][Y + i] == "#":
        break
    else:
        ans += 1
for i in range(W + 2):
    if maps[X][Y - i] == "#":
        break
    else:
        ans += 1
print(ans)
