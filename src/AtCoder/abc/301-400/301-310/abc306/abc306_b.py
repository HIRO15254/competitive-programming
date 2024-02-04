A = list(map(int, input().split()))
n = 1
ans = 0
for i in range(64):
    ans += n * A[i]
    n *= 2
print(ans)
