H, W = map(int, input().split(" "))
m = []
l = [[1 for _ in range(W)]for _ in range(H)]
for i in range(H):
    m.append(list(input()))
for i in range(H):
    p = 0
    q = 0
    for j in range(W):
        if m[i][j] == ".":
            if p == 0:
                q = j
            p += 1
        else:
            for k in range(q, q + p):
                l[i][k] += p - 1
            p = 0
    for k in range(q, q + p):
        l[i][k] += p - 1

for i in range(W):
    p = 0
    q = 0
    for j in range(H):
        if m[j][i] == ".":
            if p == 0:
                q = j
            p += 1
        else:
            for k in range(q, q + p):
                l[k][i] += p - 1
            p = 0
    for k in range(q, q + p):
        l[k][i] += p - 1

lamp_pos = 0
for i in range(len(m)):
    lamp_pos += m[i].count('.')

n2n = [1]
for i in range(lamp_pos):
    n2n.append((n2n[-1] * 2) % (10 ** 9 + 7))

ans = 0

for i in range(H):
    for j in range(W):
        if m[i][j] == ".":
            ans += (n2n[l[i][j]] - 1) * (n2n[lamp_pos - l[i][j]])
            ans %= 10 ** 9 + 7
print(ans)
