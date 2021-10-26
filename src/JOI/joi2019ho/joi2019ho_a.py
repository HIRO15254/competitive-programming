H, W = map(int, input().split(" "))
M = []
for _ in range(H):
    M.append(input())
p = [[0] * (W + 1) for _ in range(H + 1)]
for j in range(W):
    for i in range(H - 1, -1, -1):
        if M[i][j] == "I":
            p[i][j] = p[i + 1][j] + 1
        else:
            p[i][j] = p[i + 1][j]


q = [[0 for i in range(W + 1)]for _ in range(H + 1)]
for i in range(H):
    for j in range(W - 1, -1, -1):
        if M[i][j] == "O":
            q[i][j] = q[i][j + 1] + 1
        else:
            q[i][j] = q[i][j + 1]

ans = 0
for i in range(H):
    for j in range(W):
        if M[i][j] == "J":
            ans += p[i][j] * q[i][j]
print(ans)
