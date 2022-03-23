N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
d = dict()
d[0] = 1
r = 0
ans = 0
for i in A:
    r += i
    if r - K in d:
        ans += d[r - K]
    if r in d:
        d[r] += 1
    else:
        d[r] = 1
print(ans)
