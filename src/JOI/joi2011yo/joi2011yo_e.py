import math
from collections import deque
maps = []
H, W, N = map(int, input().split(" "))
rt = [[]for _ in range(H * W)]
check = [0] * (N + 1)
c = "S123456789"
road = "."
wall = "X"
for i in range(H):
    maps.append(list(input()))
for i in range(H):
    for j in range(W):
        if maps[i][j] != wall:
            if i != 0 and maps[i - 1][j] != wall:
                rt[i * W + j].append((i - 1) * W + j)
                rt[(i - 1) * W + j].append(i * W + j)
            if i != H - 1 and maps[i + 1][j] != wall:
                rt[i * W + j].append((i + 1) * W + j)
                rt[(i + 1) * W + j].append(i * W + j)
            if j != 0 and maps[i][j - 1] != wall:
                rt[i * W + j].append(i * W + (j - 1))
                rt[i * W + (j - 1)].append(i * W + j)
            if j != W - 1 and maps[i][j + 1] != wall:
                rt[i * W + j].append(i * W + (j + 1))
                rt[i * W + (j + 1)].append(i * W + j)
            if maps[i][j] != road:
                check[c.find(maps[i][j])] = i * W + j


def bfs(x, y):
    dis = [0] * (H * W)
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in rt[now]:
            if dis[i] == 0:
                q.append(i)
                dis[i] = dis[now] + 1
    dis[x] = 0
    return dis[y]


ans = 0
for i in range(N):
    ans += bfs(check[i], check[i + 1])
print(ans)
