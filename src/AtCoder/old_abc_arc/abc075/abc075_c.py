from collections import deque
N, M = map(int, input().split(" "))
rt = [[] for _ in range(N)]
hen = []
for i in range(M):
    a, b = map(int, input().split(" "))
    hen.append([a - 1, b - 1])
    rt[a - 1].append(b - 1)
    rt[b - 1].append(a - 1)


def bfs(x, y):
    dis = [0] * N
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in rt[now]:
            if not((now == hen[y][0] and i == hen[y][1]) or (now == hen[y][1] and i == hen[y][0])):
                if dis[i] == 0:
                    q.append(i)
                    dis[i] = 1
    return sum(dis) != len(rt)


ans = 0
for i in range(M):
    if bfs(0, i):
        ans += 1
print(ans)
