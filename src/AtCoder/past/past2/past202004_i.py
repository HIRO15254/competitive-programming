N = int(input())
A = list(map(int, input().split(" ")))
ans = [0 for _ in range(2 ** N)]
now = [[] for _ in range(N + 1)]
for i in range(2 ** N):
    now[0].append([A[i], i])
for i in range(N):
    for j in range(2 ** (N - i - 1)):
        if now[i][j * 2][0] > now[i][j * 2 + 1][0]:
            now[i + 1].append(now[i][j * 2])
            ans[now[i][j * 2 + 1][1]] = i + 1
        else:
            now[i + 1].append(now[i][j * 2 + 1])
            ans[now[i][j * 2][1]] = i + 1
ans[now[N][0][1]] = N
for i in range(2 ** N):
    print(ans[i])
