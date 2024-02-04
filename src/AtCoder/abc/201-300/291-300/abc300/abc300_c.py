H, W = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(input()) + ["."])
C.append(["."] * (W + 1))
ans = [0] * (min(H, W) + 1)
for x in range(W):
    for y in range(H):
        if C[y][x] == "#":
            siz = 0
            while C[y + siz][x + siz] == "#":
                C[y + siz][x + siz] = "."
                siz += 1
            siz_r = siz // 2
            for i in range(siz_r):
                C[y + siz_r + i + 1][x + siz_r - i - 1] = "."
                C[y + siz_r - i - 1][x + siz_r + i + 1] = "."
            ans[siz_r] += 1
print(" ".join(map(str, ans[1:])))
