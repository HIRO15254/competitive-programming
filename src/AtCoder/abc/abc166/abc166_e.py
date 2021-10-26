N = int(input())
A = list(map(int, input().rstrip().split(" ")))
DP = [0 for i in range(10 ** 9)]
ans = 0
for i in range(N):
    if i >= A[i]:
        ans += DP[i - A[i]]
    if A[i] <= N:
        DP[A[i] + i] += 1
print(ans)
