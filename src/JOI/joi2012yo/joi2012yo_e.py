from collections import deque

W, H = map(int, input().split(" "))
maps = [[0] * (W + 2)]
for i in range(H):
    maps.append([0] + list(map(int, input().split(" "))) + [0])
maps.append([0] * (W + 2))
c_l = [[False] * (W + 2) for _ in range(H + 2)]
c_l[0][0] = True
que = deque()
que.append([0, 0])
r_g = [[-1, -1], [0, -1], [-1, 0], [1, 0], [-1, 1], [0, 1]]
r_k = [[1, -1], [0, -1], [-1, 0], [1, 0], [1, 1], [0, 1]]
ans = 0
while len(que) != 0:
    x, y = que.pop()
    if y % 2 == 0:
        for i_x, i_y in r_g:
            if 0 <= x + i_x and x + i_x < W + 2 and 0 <= y + i_y and y + i_y < H + 2:
                if maps[y + i_y][x + i_x] == 0:
                    if not c_l[y + i_y][x + i_x]:
                        que.append([x + i_x, y + i_y])
                        c_l[y + i_y][x + i_x] = True
                else:
                    ans += 1
    else:
        for i_x, i_y in r_k:
            if 0 <= x + i_x and x + i_x < W + 2 and 0 <= y + i_y and y + i_y < H + 2:
                if maps[y + i_y][x + i_x] == 0:
                    if not c_l[y + i_y][x + i_x]:
                        que.append([x + i_x, y + i_y])
                        c_l[y + i_y][x + i_x] = True
                else:
                    ans += 1
print(ans)
