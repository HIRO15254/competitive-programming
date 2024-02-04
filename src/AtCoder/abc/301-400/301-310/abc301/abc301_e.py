from collections import deque

H, W, T = map(int, input().split())
A = []
SGo = [() for i in range(2)]
INF = 10 ** 18

A.append(["#"] * (W + 2))
for i in range(H):
    A.append(["#"] + list(input()) + ["#"])
    if ("S" in A[i + 1]):
        SGo[0] = (i + 1, A[i + 1].index("S"))
    if ("G" in A[i + 1]):
        SGo[1] = (i + 1, A[i + 1].index("G"))
    for j in range(W):
        if (A[i + 1][j + 1] == "o"):
            SGo.append((i + 1, j + 1))
A.append(["#"] * (W + 2))

dist = [[INF] * (len(SGo)) for _ in range(len(SGo))]

for i in range(len(SGo)):
    dist_tmp = [[INF] * (W + 2) for _ in range(H + 2)]
    q = deque([SGo[i]])
    dist_tmp[SGo[i][0]][SGo[i][1]] = 0
    while q:
        p = q.popleft()
        x, y = p[1], p[0]
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (A[y + dy][x + dx] != "#" and dist_tmp[y + dy][x + dx] == INF):
                dist_tmp[y + dy][x + dx] = dist_tmp[y][x] + 1
                q.append((y + dy, x + dx))
    for j in range(len(SGo)):
        dist[i][j] = dist_tmp[SGo[j][0]][SGo[j][1]]

o_count = len(SGo) - 2
DP = [[INF for _ in range(2 ** o_count)] for _ in range(o_count)]
for i in range(o_count):
    DP[i][2 ** i] = dist[0][i + 2]

if (dist[0][1] > T):
    print(-1)
    exit()

ans = 0
for i in range(2 ** o_count):
    for j in range(o_count):
        if DP[j][i] + dist[j + 2][1] <= T:
            bits = 0
            for k in range(o_count):
                if (i & (1 << k) != 0):
                    bits += 1
            ans = max(ans, bits)
        if (DP[j][i] == INF):
            continue
        for k in range(o_count):
            if (i & (1 << k) != 0):
                continue
            tmp = DP[j][i] + dist[j + 2][k + 2]
            if (tmp < DP[k][i | (1 << k)]):
                DP[k][i | (1 << k)] = tmp
print(ans)
