N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

if C.count(T) == 0:
    T = C[0]
ans = (-1, -1)
for i in range(N):
    if C[i] == T:
        if ans[0] < R[i]:
            ans = (R[i], i)
print(ans[1] + 1)
