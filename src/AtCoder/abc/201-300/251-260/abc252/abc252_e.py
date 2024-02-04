import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
penalty = [-1 for _ in range(N)]
penalty[0] = 0
li = []
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append([B, C, i + 1])
    graph[B].append([A, C, i + 1])
now = 0
ans = []
for _ in range(N - 1):
    for i in graph[now]:
        heapq.heappush(li, [i[1] + penalty[now], i[0], i[2]])
    s = heapq.heappop(li)
    while penalty[s[1]] != -1:
        s = heapq.heappop(li)
    now = s[1]
    penalty[s[1]] = s[0]
    ans.append(s[2])
print(" ".join(list(map(str, ans))))