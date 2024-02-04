import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    U, V, W = map(int, input().split())
    graph[U - 1].append((V - 1, W, i))
    graph[V - 1].append((U - 1, W, i))
K = int(input())
A = list(map(int, input().split()))
D = int(input())
X = list(map(int, input().split()))

heap = [[10 ** 18, 0, i] for i in range(N)]
ans = [-1] * N
for i in A:
    heap[i - 1] = [0, 0, i - 1]
heapq.heapify(heap)
searched = set()


def infect_day(now, dist):
    if now[1] + dist <= X[now[0]]:
        return [now[0], now[1] + dist]
    else:
        for i in range(now[0] + 1, D):
            if dist <= X[i]:
                return [i, dist]
        return [10 ** 18, 0]


while heapq:
    now = heapq.heappop(heap)
    while now[2] in searched:
        now = heapq.heappop(heap)
    for to, w, edge in graph[now]:
        inf_day = infect_day(heap[now], w)
        if ans[to] > inf_day:
            ans[to] = inf_day
            heapq.heappush(ans, inf_day + [to])


for i in range(N):
    if ans[i][0] == 10 ** 18:
        print(-1)
    else:
        print(ans[i][0])
