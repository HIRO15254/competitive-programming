H, W = map(int, input().rstrip().split())
M = [[False for _ in range(W)]for _ in range(H)]
que = []
k = [0, 0, 0]
counter = 0
for i in range(H):
    S = input()
    for i2 in range(W):
        if S[i2] == "#":
            M[i][i2] = True
            que.append([i, i2, 0])
while counter != H * W:
    k = que[counter]
    if(k[0] + 1 != H and M[k[0] + 1][k[1]] is False):
        M[k[0] + 1][k[1]] = True
        que.append([k[0] + 1, k[1], k[2] + 1])
    if(k[0] - 1 != -1 and M[k[0] - 1][k[1]] is False):
        M[k[0] - 1][k[1]] = True
        que.append([k[0] - 1, k[1], k[2] + 1])
    if(k[1] + 1 != W and M[k[0]][k[1] + 1] is False):
        M[k[0]][k[1] + 1] = True
        que.append([k[0], k[1] + 1, k[2] + 1])
    if(k[1] - 1 != -1 and M[k[0]][k[1] - 1] is False):
        M[k[0]][k[1] - 1] = True
        que.append([k[0], k[1] - 1, k[2] + 1])
    counter += 1
print(k[2])
