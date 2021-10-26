import math
N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += (i + N - N % i) * ((N - N % i - i) / i + 1) / 2
print(int(ans))
