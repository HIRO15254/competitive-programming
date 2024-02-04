import itertools


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if(a < b):
        q = a
        a = b
        b = q
    while(b > 0):
        r = a % b
        a = b
        b = r
    return a


def gcdp(p):
    g = gcd(p[0], p[1])
    if g == 0:
        return p
    return [p[0] // g, p[1] // g]


N = int(input())
points = []
gps = [[[0, 0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    points.append(list(map(int, input().split(" "))))
ans = 0

for i in range(N):
    for j in range(N):
        gps[i][j] = gcdp([points[i][0] - points[j][0], points[i][1] - points[j][1]])
for i in itertools.combinations(range(N), 3):
    if gps[i[0]][i[1]] != gps[i[1]][i[2]] and gps[i[1]][i[2]] != gps[i[2]][i[0]] and gps[i[2]][i[0]] != gps[i[0]][i[1]]:
        ans += 1
print(ans)
