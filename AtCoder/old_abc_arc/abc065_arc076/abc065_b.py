N = int(input())
A = [0]
ans = 0
i = 1
q = [False for _ in range(N + 1)]
for i in range(N):
    A.append(int(input()))
i = 1
while q[A[i]] is False:
    q[A[i]] = True
    ans += 1
    i = A[i]
    if i == 2:
        break
if i == 2:
    print(ans)
else:
    print(-1)
