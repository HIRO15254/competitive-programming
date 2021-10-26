N, K = map(int, input().rstrip().split(" "))
ans = 0
for i in range(K, N + 2):
    ans = (ans + (i * N) - (i * (i - 1)) + 1) % 1000000007
print(ans)
