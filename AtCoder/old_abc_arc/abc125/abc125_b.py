N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += max(A[i] - C[i], 0)
print(ans)
