H, W, N = map(int, input().split())

ans = [["." for _ in range(W)] for _ in range(H)]

now_x = 0
now_y = 0
now_ang = 0
ang = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(N):
    if ans[now_y][now_x] == ".":
        ans[now_y][now_x] = "#"
        now_ang += 1
    else:
        ans[now_y][now_x] = "."
        now_ang -= 1
    now_ang %= 4
    now_x += ang[now_ang][1]
    now_y += ang[now_ang][0]
    if now_x < 0:
        now_x = W - 1
    if now_x >= W:
        now_x = 0
    if now_y < 0:
        now_y = H - 1
    if now_y >= H:
        now_y = 0

for i in range(H):
    print("".join(ans[i]))
