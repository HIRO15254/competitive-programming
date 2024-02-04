N = int(input())
A = list(map(int, input().split()))
A.sort()
mod = 998244353

dp = [1]
now = 1
i = 0
now_count = 0

while (i < N) or (len(dp) > 1):
    now_count = 0
    while i < N and A[i] == now:
        now_count += 1
        i += 1
    max_next_dp = (len(dp) - 1 + now_count) // 2
    next_dp = [0] * (max_next_dp + 1)
    for j in range(len(dp)):
        next_dp[(j + now_count) // 2] += dp[j]
    next_dp_2 = [0] * (max_next_dp + 1)
    imos_count = 0
    for j in range(max_next_dp + 1):
        imos_count += next_dp[-(1 + j)]
        imos_count %= mod
        next_dp_2[-(1 + j)] = imos_count
    dp = next_dp_2
    now += 1
print(dp[0] % mod)
