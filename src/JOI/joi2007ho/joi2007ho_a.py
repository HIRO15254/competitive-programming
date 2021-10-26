n, k = map(int, input().split(" "))
A = []
for i in range(n):
    A.append(int(input()))
q = 0
ans = 0
for i in range(k):
    q += A[i]
ans = q
for i in range(n - k - 1):
    q -= A[i]
    q += A[k + i]
    ans = max(ans, q)
print(ans)
