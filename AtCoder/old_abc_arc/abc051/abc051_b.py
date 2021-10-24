K, N = map(int, input().rstrip().split(" "))
ans = 0
for i in range(K + 1):
    for i2 in range(K + 1):
        if i + i2 <= N and N - i - i2 <= K:
            ans += 1
print(ans)
