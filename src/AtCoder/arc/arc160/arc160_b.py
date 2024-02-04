T = int(input())
mod = 998244353
for i in range(T):
    N = int(input())
    ans = 0
    # x > y > z
    y = 1
    while y ** 2 <= N:
        ans += (N // y - y) * (y - 1) * 6
        ans += (y - 1) * 3
        ans += (N // y - y) * 3
        ans += 1
        ans %= mod
        y += 1
    print(ans)
