T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    now = N
    for i in range(N - 1, -1, -1):
        if A[i] <= i + 1 and A[i] <= now:
            ans += 1
            now = A[i]
    print(ans)
