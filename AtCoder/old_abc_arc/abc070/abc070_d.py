from collections import deque
N = int(input())
rt = [[] for _ in range(N)]
for i in range(N - 1):
    a, b, c = map(int, input().split(" "))
    rt[a - 1].append([b - 1, c])
    rt[b - 1].append([a - 1, c])


def bfs(x):
    dis = [0] * N
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in rt[now]:
            if dis[i[0]] == 0:
                q.append(i[0])
                dis[i[0]] = dis[now] + i[1]
    dis[x] = 0
    return dis


Q, K = map(int, input().split(" "))
dis = bfs(K - 1)
for i in range(Q):
    x, y = map(int, input().split(" "))
    print(dis[x - 1] + dis[y - 1])
