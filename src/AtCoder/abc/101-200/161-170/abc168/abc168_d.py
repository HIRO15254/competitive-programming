from collections import deque

N, M = map(int, input().rstrip().split(" "))
A = [[] for i in range(N)]
closest = [-1 for i in range(N)]
closest[0] = 0
ans = [-1 for i in range(N)]
que = deque([[0, 0]])
for i in range(M):
    q, qq = map(int, input().rstrip().split(" "))
    A[q - 1].append(qq - 1)
    A[qq - 1].append(q - 1)
while len(que) != 0:
    for i in A[que[0][0]]:
        if closest[i] == -1:
            closest[i] = que[0][1] + 1
            ans[i] = que[0][0] + 1
            que.append([i, que[0][1] + 1])
    que.popleft()
print("Yes")
for i in range(N - 1):
    print(ans[i + 1])
