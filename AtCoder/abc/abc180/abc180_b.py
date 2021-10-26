import math
N = int(input())
A = list(map(int, input().split(" ")))
ans = 0
for i in A:
    ans += abs(i)
print(ans)

ans = 0
for i in A:
    ans += i ** 2
print(math.sqrt(ans))

ans = 0
for i in A:
    ans = max(ans, abs(i))
print(ans)
