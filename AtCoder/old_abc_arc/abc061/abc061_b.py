N, M = map(int, input().split())
ans = [0 for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    ans[a - 1] += 1
    ans[b - 1] += 1
for i in range(N):
    print(ans[i])
