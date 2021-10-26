N, X, Y = map(int, input().rstrip().split())
ans = [0 for _ in range(N)]
dis = [0, 0]
xycent = (X + Y) / 2
for i in range(1, N):
    for i2 in range(i + 1, N + 1):
        dis[0] = i2 - i
        dis[1] = abs(i - X) + abs(i2 - Y) + 1
        if dis[0] > dis[1]:
            ans[dis[1]] += 1
        else:
            ans[dis[0]] += 1
for i in range(1, N):
    print(ans[i])
