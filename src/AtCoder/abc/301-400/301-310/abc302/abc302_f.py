from collections import deque
INF = 10 ** 18

N, M = map(int, input().split())
e = [[] for _ in range(M + N + 1)]
d = [INF] * (M + N + 1)

for i in range(N):
    A = int(input())
    S = list(map(int, input().split()))
    e[M + 1 + i] = S
    for j in S:
        e[j].append(M + 1 + i)

d[1] = 0
q = deque([1])
while q:
    v = q.popleft()
    for i in e[v]:
        if d[i] == INF:
            d[i] = d[v] + 1
            q.append(i)
if d[M] == INF:
    print(-1)
else:
    print(d[M] // 2 - 1)
