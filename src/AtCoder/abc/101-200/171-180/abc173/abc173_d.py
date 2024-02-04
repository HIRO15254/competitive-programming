from collections import deque
N = int(input())
A = list(map(int, input().rstrip().split(" ")))
A.sort(reverse=True)
ans = 0
que = deque()
que.append(A[0])
for i in range(1, len(A)):
    ans += que[0]
    que.popleft()
    que.append(A[i])
    que.append(A[i])
print(ans)
