from collections import deque

N1, N2, M = map(int, input().split())

graph1 = [[] for _ in range(N1)]
graph2 = [[] for _ in range(N2)]


def max_dfs(graph, start):
    q = deque()
    q.append(start)
    dis = [-1] * len(graph)
    dis[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == -1:
                dis[i] = dis[now] + 1
                q.append(i)
    return max(dis)


for i in range(M):
    a, b = map(int, input().split())
    if a < N1:
        graph1[a - 1].append(b - 1)
        graph1[b - 1].append(a - 1)
    else:
        graph2[a - N1 - 1].append(b - N1 - 1)
        graph2[b - N1 - 1].append(a - N1 - 1)

print(max_dfs(graph1, 0) + max_dfs(graph2, N2 - 1) + 1)
