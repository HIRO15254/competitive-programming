from collections import deque
N, X, Y = map(int, input().rstrip().split(" "))
# 0=なし -1=障害物 0,未探索 1以上、距離　※座標に必ず210足す！
maps = [[0 for _ in range(420)] for _ in range(420)]
que = deque([[210, 210]])
kin = [[1, 1], [0, 1], [-1, 1], [1, 0], [-1, 0], [0, -1]]
for i in range(N):
    s = list(map(int, input().rstrip().split(" ")))
    maps[s[0] + 210][s[1] + 210] = -1
maps[210][210] = 1
while maps[X + 210][Y + 210] == 0 and len(que) != 0:
    for i in range(6):
        if 0 < que[0][0] + kin[i][0] < 419 and 0 < que[0][1] + kin[i][1] < 419 and maps[que[0][0] + kin[i][0]][que[0][1] + kin[i][1]] == 0:
            que.append([que[0][0] + kin[i][0], que[0][1] + kin[i][1]])
            maps[que[0][0] + kin[i][0]][que[0][1] + kin[i]
                                        [1]] = maps[que[0][0]][que[0][1]] + 1
    que.popleft()
if maps[X + 210][Y + 210] == 0:
    print(-1)
else:
    print(maps[X + 210][Y + 210] - 1)
