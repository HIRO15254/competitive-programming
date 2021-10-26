import math
ans = 0
n = int(input())
K = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for i2 in range(1, n + 1):
        K[math.gcd(i, i2)] += 1
for i in range(1, n + 1):
    for i2 in range(1, n + 1):
        ans += K[i] * math.gcd(i, i2)
print(ans)
