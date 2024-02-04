N = int(input())
ans = 0
for i in range(N):
    ans += N / (i + 1)
print(ans - 1)
