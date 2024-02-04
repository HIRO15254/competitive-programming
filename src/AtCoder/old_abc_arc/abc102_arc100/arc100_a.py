N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= i + 1
A.sort()
b = A[N // 2]
ans = 0
for i in A:
    ans += abs(i - b)
print(ans)
