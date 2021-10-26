N, M, D = map(int, input().split(" "))
ma = []
for i in range(N):
    ma.append(list(input()))
ans = 0
for i in range(N):
    if M < D:
        break
    for j in range(M - D + 1):
        for k in range(D):
            if ma[i][j + k] == "#":
                break
        else:
            ans += 1

for i in range(M):
    if N < D:
        break
    for j in range(N - D + 1):
        for k in range(D):
            if ma[j + k][i] == "#":
                break
        else:
            ans += 1

print(ans)
