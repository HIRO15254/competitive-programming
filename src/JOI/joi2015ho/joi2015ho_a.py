N, M = map(int, input().split(" "))
P = list(map(int, input().split(" ")))
p = []
q = [0 for i in range(N)]
r = [0 for i in range(N)]
for i in range(N - 1):
    a, b, c = map(int, input().split(" "))
    p.append([a, b, c])

for i in range(M - 1):
    q[min(P[i], P[i + 1]) - 1] += 1
    q[max(P[i], P[i + 1]) - 1] -= 1
ans = 0
for i in range(N - 1):
    r[i] = r[i - 1] + q[i]
    ans += min(p[i][0] * r[i], p[i][1] * r[i] + p[i][2])

print(ans)
