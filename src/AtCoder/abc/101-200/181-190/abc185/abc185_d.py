N, M = map(int, input().split(" "))

if M != 0:
    A = list(map(int, input().split(" ")))
else:
    A = []
A.append(0)
A.append(N + 1)

A.sort()
q = []
for i in range(M + 1):
    if A[i + 1] - A[i] != 1:
        q.append(A[i + 1] - A[i] - 1)
if len(q) == 0:
    print(0)
else:
    r = min(q)
    ans = 0
    for i in q:
        ans += (i - 1) // r + 1
    print(ans)
