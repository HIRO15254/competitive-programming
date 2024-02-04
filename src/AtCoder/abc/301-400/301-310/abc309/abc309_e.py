from collections import deque

N, M = map(int, input().split())
p = list(map(int, input().split()))
rest = [-1] * N

for i in range(M):
    x, y = map(int, input().split())
    rest[x - 1] = max(rest[x - 1], y)

c = [[] for _ in range(N)]
for i in range(N - 1):
    c[p[i] - 1].append(i + 1)

q = deque([0])
while q:
    now = q.popleft()
    for i in c[now]:
        q.append(i)
        rest[i] = max(rest[i], rest[now] - 1)
print(N - rest.count(-1))
