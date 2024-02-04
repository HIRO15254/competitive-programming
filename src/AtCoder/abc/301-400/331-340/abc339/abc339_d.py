from collections import deque

N = int(input())
dp = [[[[-1 for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]

grid = []
init_p = []

for i in range(N):
    g = list(input())
    for j in range(N):
        if g[j] == "P":
            init_p.append(i)
            init_p.append(j)
            g[j] = "."
    grid.append(g)

q = deque()
q.append((init_p[0], init_p[1], init_p[2], init_p[3]))
dp[init_p[0]][init_p[1]][init_p[2]][init_p[3]] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    y1, x1, y2, x2 = q.popleft()
    if y1 == y2 and x1 == x2:
        print(dp[y1][x1][y2][x2])
        break
    for i in range(4):
        ny1 = y1 + dy[i]
        nx1 = x1 + dx[i]
        ny2 = y2 + dy[i]
        nx2 = x2 + dx[i]
        can_move1 = 0 <= ny1 < N and 0 <= nx1 < N and grid[ny1][nx1] == "."
        can_move2 = 0 <= ny2 < N and 0 <= nx2 < N and grid[ny2][nx2] == "."
        if can_move1 and can_move2:
            if dp[ny1][nx1][ny2][nx2] == -1:
                dp[ny1][nx1][ny2][nx2] = dp[y1][x1][y2][x2] + 1
                q.append((ny1, nx1, ny2, nx2))
        elif can_move1:
            if dp[ny1][nx1][y2][x2] == -1:
                dp[ny1][nx1][y2][x2] = dp[y1][x1][y2][x2] + 1
                q.append((ny1, nx1, y2, x2))
        elif can_move2:
            if dp[y1][x1][ny2][nx2] == -1:
                dp[y1][x1][ny2][nx2] = dp[y1][x1][y2][x2] + 1
                q.append((y1, x1, ny2, nx2))
else:
    print(-1)
