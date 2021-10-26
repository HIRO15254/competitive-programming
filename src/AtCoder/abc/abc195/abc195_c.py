N = int(input()) + 1
ans = 0
for i in range(3, 18, 3):
    if (N > 10**i):
        ans += N - 10**i
print(ans)
