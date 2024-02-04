def gcd(a, b):
    if(a < b):
        q = a
        a = b
        b = q
    while(b > 0):
        r = a % b
        a = b
        b = r
    return a


def gen(x, y):
    a_x = abs(x)
    a_y = abs(y)
    if x != 0 and y != 0:
        a, b = a_x, a_y
        if(a < b):
            a, b = b, a
        while(b > 0):
            a, b = b, a % b
        g = a
    else:
        if a_x > a_y:
            g = a_x
        else:
            g = a_y
    return [x // g, y // g]            


N, K = map(int, input().split())
points = []
checked = [False] * (N * N)
for i in range(N):
    for j in range(i, N):
        checked[i + j * N] = True
for i in range(N):
    X, Y = map(int, input().split())
    points.append([X, Y])
cache = []
for i in range(N):
    for j in range(N):
        if i == j:
            cache.append([0, 0])
        else:
            cache.append(gen(points[i][0] - points[j][0], points[i][1] - points[j][1]))
if K == 1:
    print("Infinity")
else:
    ans = 0
    for i in range(N):
        for j in range(i):
            if not checked[i + j * N]:
                col = [j, i]
                ij = cache[i + j * N]
                ij_m = [-ij[0], -ij[1]]
                for k in range(i + 1, N):
                    ik = cache[i + k * N]
                    if ik == ij or ij_m == ik:
                        for m in col:
                            checked[k + m * N] = True
                        col.append(k)
                if len(col) >= K:
                    ans += 1
    print(ans)
