from collections import deque

H, W = map(int, input().split())
reachable = [[-1 for _ in range(W)] for _ in range(H)]

maze = [input() for _ in range(H)]

queue = deque()
queue.append((0, 0))
reachable[0][0] = 1


def snuke_next(s, n):
    if s == "s":
        return n == "n"
    if s == "n":
        return n == "u"
    if s == "u":
        return n == "k"
    if s == "k":
        return n == "e"
    if s == "e":
        return n == "s"


while queue:
    now = queue.popleft()
    if now[0] != 0:
        if reachable[now[0] - 1][now[1]] == -1 and snuke_next(maze[now[0]][now[1]], maze[now[0] - 1][now[1]]):
            reachable[now[0] - 1][now[1]] = 1
            queue.append((now[0] - 1, now[1]))
    if now[0] != H - 1:
        if reachable[now[0] + 1][now[1]] == -1 and snuke_next(maze[now[0]][now[1]], maze[now[0] + 1][now[1]]):
            reachable[now[0] + 1][now[1]] = 1
            queue.append((now[0] + 1, now[1]))
    if now[1] != 0:
        if reachable[now[0]][now[1] - 1] == -1 and snuke_next(maze[now[0]][now[1]], maze[now[0]][now[1] - 1]):
            reachable[now[0]][now[1] - 1] = 1
            queue.append((now[0], now[1] - 1))
    if now[1] != W - 1:
        if reachable[now[0]][now[1] + 1] == -1 and snuke_next(maze[now[0]][now[1]], maze[now[0]][now[1] + 1]):
            reachable[now[0]][now[1] + 1] = 1
            queue.append((now[0], now[1] + 1))
if reachable[H - 1][W - 1] == 1:
    print("Yes")
else:
    print("No")
