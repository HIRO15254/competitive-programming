
from collections import deque
H, W = map(int, input().rstrip().split(" "))
dist = [[-1] * W for _ in range(H)]
maps = []
used = [True] * 26
alp = list("abcdefghijklmnopqrstuvwxyz")
warp = [[] for i in range(26)]

for i in range(H):
    maps.append(list(input()))

Sh, Sw = 0, 0
Gh, Gw = 0, 0
for i in range(H):
    for j in range(W):
        if maps[i][j] == ".":
            continue
        elif maps[i][j] == "#":
            continue
        elif maps[i][j] == "S":
            Sh, Sw = i, j
        elif maps[i][j] == "G":
            Gh, Gw = i, j
        else:
            for k in range(26):
                if maps[i][j] == alp[k]:
                    warp[k].append([i, j])
                    break

que = deque()
que.append([Sh, Sw])
dist[Sh][Sw] = 0

while que:
    h, w = que.popleft()
    if h + 1 < H:
        if dist[h + 1][w] == -1 and maps[h + 1][w] != "#":
            dist[h + 1][w] = dist[h][w] + 1
            que.append([h + 1, w])
    if h - 1 >= 0:
        if dist[h - 1][w] == -1 and maps[h - 1][w] != "#":
            dist[h - 1][w] = dist[h][w] + 1
            que.append([h - 1, w])
    if w + 1 < W:
        if dist[h][w + 1] == -1 and maps[h][w + 1] != "#":
            dist[h][w + 1] = dist[h][w] + 1
            que.append([h, w + 1])
    if w - 1 >= 0:
        if dist[h][w - 1] == -1 and maps[h][w - 1] != "#":
            dist[h][w - 1] = dist[h][w] + 1
            que.append([h, w - 1])
    if maps[h][w] != "." and maps[h][w] != "S" and maps[h][w] != "G":
        q = alp.index(maps[h][w])
        if used[q]:
            for h2, w2 in warp[q]:
                if dist[h2][w2] == -1:
                    dist[h2][w2] = dist[h][w] + 1
                    que.append([h2, w2])
            used[q] = False
print(dist[Gh][Gw])
