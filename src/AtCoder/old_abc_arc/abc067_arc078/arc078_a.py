N = int(input())
a = list(map(int, input().rstrip().split(" ")))
K = sum(a)
now = 0
ans = 10 ** 15
for i in range(N - 1):
    now += a[i]
    K -= a[i]
    ans = min(ans, abs(K - now))
print(ans)
