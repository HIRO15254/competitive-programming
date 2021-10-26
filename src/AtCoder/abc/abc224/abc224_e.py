H, W, N = map(int, input().split(" "))
H_max = [0] * H
H_update = []
W_max = [0] * W
W_update = []
ans = [0] * N
points = []
for i in range(N):
    r, c, a = map(int, input().split(" "))
    points.append([a, r - 1, c - 1, i])
points.sort(reverse=True)

last = 10 ** 18
for p in points:
    if p[0] != last:
        for i in H_update:
            H_max[i[0]] = max(H_max[i[0]], i[1])
        H_update = []
        for i in W_update:
            W_max[i[0]] = max(W_max[i[0]], i[1])
        W_update = []
    ans[p[3]] = max(H_max[p[1]], W_max[p[2]])
    H_update.append([p[1], ans[p[3]] + 1])
    W_update.append([p[2], ans[p[3]] + 1])
    last = p[0]
for i in ans:
    print(i)
