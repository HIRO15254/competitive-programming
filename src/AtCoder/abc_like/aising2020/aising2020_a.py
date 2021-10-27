L, R, D = map(int, input().rstrip().split(" "))
ans = 0
for i in range(L, R + 1):
    if i % D == 0:
        ans += 1
print(ans)
