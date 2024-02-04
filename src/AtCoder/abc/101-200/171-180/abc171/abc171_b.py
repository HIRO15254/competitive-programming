N, K = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
ans = 0
A.sort()
for i in range(K):
    ans += A[i]
print(ans)
