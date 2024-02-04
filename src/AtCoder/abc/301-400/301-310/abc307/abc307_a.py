N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
for i in range(N):
    for j in range(7):
        ans[i] += A[i * 7 + j]
print(" ".join(map(str, ans)))
