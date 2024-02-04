N = int(input())
dp = [False] * 101
dp[0] = True
for i in range(100):
    if dp[i]:
        if i + 4 <= 100:
            dp[i + 4] = True
        if i + 7 <= 100:
            dp[i + 7] = True
print('Yes' if dp[N] else 'No')
