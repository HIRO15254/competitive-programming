H, W = map(int, input().split(" "))
m = []
for i in range(H):
    m.append(list(input()))
ans = 0
for i in range(H):
    for j in range(W - 1):
        if m[i][j] == "." and m[i][j + 1] == ".":
            ans += 1
for i in range(H - 1):
    for j in range(W):
        if m[i][j] == "." and m[i + 1][j] == ".":
            ans += 1
print(ans)
