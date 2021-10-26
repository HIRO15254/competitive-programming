N = int(input())


def warshall_floid(d):
    r = [[10 ** 10] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                r[i][j] = min(r[i][j], d[i][k] + d[k][j])
    return r


d = [[10 ** 10] * N for _ in range(N)]
for i in range(N):
    d[i] = list(map(int, input().split(" ")))
if d != warshall_floid(d):
    print(-1)
else:
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                if d[i][k] + d[j][k] <= d[i][j]:
                    if k != i and k != j:
                        break
            else:
                ans += d[i][j]
    print(ans)
