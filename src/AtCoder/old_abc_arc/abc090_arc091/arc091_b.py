N, K = map(int, input().split(" "))
ans = 0
for b in range(K + 1, N + 1):
    q = N % b
    p = N // b
    ans += p * (b - K) + max(0, q - max(1, K) + 1)
print(ans)
