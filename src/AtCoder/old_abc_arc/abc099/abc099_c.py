MAX = 10 ** 5
able = [1]
now = 6
while now <= MAX:
    able.append(now)
    now *= 6
now = 9
while now <= MAX:
    able.append(now)
    now *= 9
able.sort()

dp = [-1] * (MAX + 1)
dp[0] = 0
for i in range(MAX):
    for j in able:
        if i + j > MAX:
            break
        if dp[i + j] == -1:
            dp[i + j] = dp[i] + 1
        else:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
print(dp[int(input())])
