from sys import stdin
input = stdin.readline

ans = 0

R, C = map(int, input().split(" "))
Sen = []
for i in range(R):
    Sen.append(list(map(int, input().split(" "))))

P = [0 for i in range(2 ** R)]
k = 0
for i in range(C):
    k = 0
    for j in range(R):
        if Sen[j][i] == 1:
            k += 1 << j
    P[k] += 1

for i in range(2 ** R):
    q = [0] * 2 ** R
    for j in range(2 ** R):
        for k in range(R):
            if (i >> k) & 1 == (j >> k) & 1:
                q[j] += 1
        if q[j] < R / 2:
            q[j] = R - q[j]
    p = 0
    for j in range(2 ** R):
        p += q[j] * P[j]
    ans = max(ans, p)
print(ans)
