L, R = map(int, input().split())
ans = 10 ** 18
R = min(L + 2019, R)
for i in range(L, R):
    for j in range(i + 1, R + 1):
        ans = min((i * j) % 2019, ans)
print(ans)
