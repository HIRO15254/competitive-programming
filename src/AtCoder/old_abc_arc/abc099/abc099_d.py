import itertools

INF = 10 ** 18
N, C = map(int, input().split())
D = []
for _ in range(C):
    D.append(list(map(int, input().split())))
c = []
for _ in range(N):
    c.append(list(map(int, input().split())))

ans = INF
iwa = [[0] * C for _ in range(3)]
for col in range(C):
    for i in range(N):
        for j in range(N):
            iwa[(i + j) % 3][col] += D[c[i][j] - 1][col]
for col in itertools.permutations(range(C), 3):
    now_iwa = 0
    for i in range(3):
        now_iwa += iwa[i][col[i]]
    ans = min(ans, now_iwa)
print(ans)
