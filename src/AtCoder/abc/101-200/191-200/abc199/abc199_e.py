import itertools
N, M = map(int, input().split(" "))
fi = [[] for _ in range(N + 1)]
for i in range(M):
    X, Y, Z = map(int, input().split(" "))
    fi[X].append([Y - 1, Z])

DP = [dict() for _ in range(N + 1)]

for i in range(N + 1):
    for j in itertools.combinations(range(N), i):
        p = 0
        for k in j:
            p += 2 ** k
        DP[i][p] = 0
DP[0][0] = 1


def C(k, j):
    p = []
    for i in range(N):
        if (j >> i) & 1:
            p.append(i)
    p.sort()
    for i in fi[k]:
        if i[1] < k:
            if p[i[1]] <= i[0]:
                return False
    return True


for i in range(N):
    for j in DP[i].keys():
        for k in range(N):
            if not (j >> k) & 1:
                if C(i + 1, j + (2**k)):
                    DP[i + 1][j + (2**k)] += DP[i][j]

ans = 0
for i in DP[-1].values():
    ans += i
print(ans)
