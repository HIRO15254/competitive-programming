N = int(input())
S1 = []
S2 = []
ans = [0, 1, 1, 2]
for i in range(N):
    S1.append(list(input()))
for i in range(N):
    S2.append(list(input()))
for i in range(N):
    for i2 in range(N):
        if S1[i][i2] != S2[i][i2]:
            ans[0] += 1
for i in range(N):
    for i2 in range(N):
        if S1[i2][N - i - 1] != S2[i][i2]:
            ans[1] += 1
for i in range(N):
    for i2 in range(N):
        if S1[N - i2 - 1][i] != S2[i][i2]:
            ans[2] += 1
for i in range(N):
    for i2 in range(N):
        if S1[N - i - 1][N - i2 - 1] != S2[i][i2]:
            ans[3] += 1
print(min(ans))
