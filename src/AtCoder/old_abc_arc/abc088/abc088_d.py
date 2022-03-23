from collections import deque


def GridEdge(H, W, grid, wall="#", move=[[1, 0], [-1, 0], [0, 1], [0, -1]]):
    """グリッド問題をグラフに起こす関数。点(x, y)に頂点(y * W + x)が対応している"""
    graph = [[] for _ in range(H * W)]
    for y in range(H):
        for x in range(W):
            if grid[y][x] != wall:
                for i in move:
                    xd = x + i[1]
                    yd = y + i[0]
                    if 0 <= xd and xd < W and 0 <= yd and yd < H:
                        if grid[yd][xd] != wall:
                            n = y * W + x
                            nd = yd * W + xd
                            graph[n].append(nd)
    return graph


def bfs(N, graph, x, INF=-1):
    """bfsによる最短経路探索"""
    dis = [INF] * N
    dis[x] = 0
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == INF:
                q.append(i)
                dis[i] = dis[now] + 1
    return dis


H, W = map(int, input().split(" "))
grid = []
ans = 0
for _ in range(H):
    grid.append(list(input()))
    ans += grid[-1].count(".")
graph = GridEdge(H, W, grid)
dist = bfs(H * W, graph, 0)[W * H - 1]
if dist == -1:
    print(-1)
else:
    print(ans - dist - 1)
