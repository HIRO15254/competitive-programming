N, M, Q = map(int, input().rstrip().split(" "))
i = 0
K = []

A = [1] * N
A.append(M)
E = [M] * (N + 1)

q = []

karians = 0
ans = 0
for _ in range(Q):
    q.append(list(map(int, input().split(" "))))

while True:
    karians = 0
    for qq in q:
        if A[qq[1] - 1] - A[qq[0] - 1] == qq[2]:
            karians += qq[3]
    if karians > ans:
        ans = karians
    if A == E:
        break
    i = 0
    A[0] += 1
    while A[i] == A[i + 1] + 1:
        A[i] = 1
        A[i + 1] += 1
        i += 1
        if i == N - 1:
            break
print(ans)
