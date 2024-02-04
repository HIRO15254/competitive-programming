H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]
C = [[False for _ in range(W)] for _ in range (H)]
now = [0, 0]
move = [0, 0]
while not C[now[0]][now[1]]:
    if G[now[0]][now[1]] == 'U':
        move = [-1, 0]
    elif G[now[0]][now[1]] == 'D':
        move = [1, 0]
    elif G[now[0]][now[1]] == 'L':
        move = [0, -1]
    elif G[now[0]][now[1]] == 'R':
        move = [0, 1]
    if 0 <= now[0] + move[0] and now[0] + move[0] < H and 0 <= now[1] + move[1] and now[1] + move[1] < W:
        C[now[0]][now[1]] = True
        now[0] += move[0]
        now[1] += move[1]
    else:
        print(now[0] + 1, now[1] + 1)
        break
else:
    print(-1)
