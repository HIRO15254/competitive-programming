n = int(input())
a = list(map(int, input().rstrip().split(" ")))
q = 0
ans = 0
ans2 = 0
for i in range(n):
    q += a[i]
    if i % 2 == 0:
        if q <= 0:
            ans += 1 - q
            q = 1
    else:
        if q >= 0:
            ans += 1 + q
            q = -1
q = 0
for i in range(n):
    q += a[i]
    if i % 2 == 1:
        if q <= 0:
            ans2 += 1 - q
            q = 1
    else:
        if q >= 0:
            ans2 += 1 + q
            q = -1
print(min(ans, ans2))
