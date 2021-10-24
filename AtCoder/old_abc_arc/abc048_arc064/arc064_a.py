N, x = map(int, input().rstrip().split(" "))
ans = 0
A = list(map(int, input().rstrip().split(" ")))
if A[0] > x:
    ans += A[0] - x
    A[0] = x
for i in range(N - 1):
    k = max(A[i] + A[i + 1] - x, 0)
    ans += k
    A[i + 1] -= k
print(ans)
