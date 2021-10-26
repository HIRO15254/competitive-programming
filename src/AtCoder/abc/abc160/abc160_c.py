K, N = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
A.append(A[0] + K)
ans = 0
for i in range(N):
    if A[i + 1] - A[i] > ans:
        ans = A[i + 1] - A[i]
print(K - ans)
