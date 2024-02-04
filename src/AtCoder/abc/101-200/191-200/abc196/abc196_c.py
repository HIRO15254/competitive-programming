N = int(input())
ans = 0
for i in range(1, 10 ** 6):
    k = str(i) * 2
    p = int(k)
    if p <= N:
        ans += 1
print(ans)
