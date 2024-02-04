from collections import deque
from operator import le
N, M = map(int, input().split(" "))
INF = 10 ** 18
pos = [-INF] * N
info = [[] for _ in range(N)]
left = set()
for i in range(M):
    L, R, D = map(int, input().split(" "))
    info[L - 1].append([R - 1, D])
    info[R - 1].append([L - 1, -D])
    left.add(L - 1)
    left.add(R - 1)
while left:
    for i in left:
        start = i
        break
    left.discard(start)
    que = deque()
    pos[start] = 0
    que.append(start)
    while que:
        now = que.popleft()
        for i in info[now]:
            if pos[i[0]] == -INF:
                pos[i[0]] = pos[now] + i[1]
                que.append(i[0])
                left.discard(i[0])
            else:
                if pos[i[0]] != pos[now] + i[1]:
                    print("No")
                    exit()
print("Yes")
