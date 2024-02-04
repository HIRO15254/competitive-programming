from collections import deque

N = int(input())
A = list(map(int, input().split()))
G = []
for _ in range(N):
    G.append(input())

ans = [[[-1, 0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    ans[i][i] = [0, A[i]]

for i in range(N):
    q = deque()
    q.append(i)
    while(q):
        now = q.popleft()
        for j in range(N):
            if G[now][j] == "Y" and i != j:
                if ans[i][j][0] == -1:
                    ans[i][j] = [ans[i][now][0] + 1, ans[i][now][1] + A[j]]
                    q.append(j)
                elif ans[i][j][0] > ans[i][now][0] + 1:
                    ans[i][j] = [ans[i][now][0] + 1, ans[i][now][1] + A[j]]
                elif ans[i][j][0] == ans[i][now][0] + 1:
                    ans[i][j][1] = max(ans[i][j][1], ans[i][now][1] + A[j])
Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    if ans[U - 1][V - 1][0] == -1:
        print("Impossible")
    else:
        print(ans[U - 1][V - 1][0], ans[U - 1][V - 1][1])
