from collections import deque

N = int(input())
M = N - 1
graph = [[] for _ in range(N + 1)]
dis_f = []
dis_s = []

# フェネックの距離
for i in range(M):
    a, b = map(int, input().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)

dist_f = [-1] * (N + 1)
dist_f[0] = 0
dist_f[1] = 0
d = deque()
d.append(1)
left = N - 1
while(d):
    v = d.popleft()
    for i in graph[v]:
        if dist_f[i] != -1:
            continue
        dist_f[i] = dist_f[v] + 1
        d.append(i)

# すぬけくんの距離

dist = [-1] * (N + 1)
dist[0] = 0
dist[N] = 0
d = deque()
d.append(N)
while(d):
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

count_f = 0
count_s = 0
for i in range(N):
    if(dist_f[i + 1] <= dist[i + 1]):
        count_f += 1
    else:
        count_s += 1
if(count_f > count_s):
    print("Fennec")
else:
    print("Snuke")
