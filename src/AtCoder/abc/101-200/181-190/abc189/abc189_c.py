N = int(input())
A = list(map(int, input().split(" ")))
ans = 0
for l in range(N):
    min_now = A[l]
    for r in range(l, N):
        min_now = min(min_now, A[r])
        ans = max(min_now * (r - l + 1), ans)
print(ans)
