H, W, K = map(int, input().rstrip().split(" "))
s = []
ans = 0
for i in range(H):
    s.append(list(input()))

for i in range(2 ** H):
    l = [0 for i in range(W)]
    for i2 in range(H):
        if (i >> i2) & 1:
            for i3 in range(W):
                if s[i2][i3] == "#":
                    l[i3] += 1
    for i2 in range(2 ** W):
        q = 0
        for i3 in range(W):
            if (i2 >> i3) & 1:
                q += l[i3]
        if q == K:
            ans += 1
print(ans)
