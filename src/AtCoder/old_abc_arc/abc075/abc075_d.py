N, K = map(int, input().split(" "))
points = []
points2 = []
xlist = []
ylist = []
for _ in range(N):
    x, y = map(int, input().split(" "))
    points.append([x, y])
    xlist.append(x)
    ylist.append(y)
xlist.sort()
ylist.sort()
rw = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    points2.append([xlist.index(points[i][0]), ylist.index(points[i][1])])
points2.sort()
for i in range(N):
    c = False
    for j in range(N):
        if points2[i][1] == j:
            c = True
        if c:
            rw[i + 1][j + 1] = rw[i][j + 1] + 1
        else:
            rw[i + 1][j + 1] = rw[i][j + 1]
ans = 10 ** 19
for i in range(N):
    for j in range(i, N):
        for k in range(N):
            for l in range(k, N):
                if rw[j + 1][l + 1] + rw[i][k] - rw[j + 1][k] - rw[i][l + 1] >= K:
                    ans = min(ans, (xlist[j] - xlist[i]) * (ylist[l] - ylist[k]))
print(ans)
