H, W = map(int, input().split(" "))
n = 10


def warshall_floid(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


d = [[0] * n for i in range(n)]
for i in range(n):
    d[i] = list(map(int, input().split(" ")))

d2 = warshall_floid(d)
c = [0] * 10
for i in range(H):
    p = list(map(int, input().split(" ")))
    for i in range(10):
        c[i] += p.count(i)

ans = 0
for i in range(10):
    ans += d[i][1] * c[i]
print(ans)
