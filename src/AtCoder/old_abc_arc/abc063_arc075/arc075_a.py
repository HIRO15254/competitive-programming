N = int(input())
DP = [False for _ in range(N * 100 + 1)]
DP[0] = True
for i in range(N):
    k = int(input())
    for i2 in range(i * 100 + 1, -1, -1):
        if DP[i2] != 0:
            DP[i2 + k] = True
ans = 0
for i in range(N * 100 + 1):
    if DP[i] is True and i % 10 != 0:
        ans = i
print(ans)
