N, K = map(int, input().split())
A = list(map(int, input().split()))

dp_elem = dict()
dp = [0] * (N + 1)
for i in A:
    for j in A:
        if i + j <= N:
            if (i + j) in dp_elem:
                dp_elem[i + j] = max(dp_elem[i + j], i)
            else:
                dp_elem[i + j] = i
for i in range(N):
    for j in dp_elem:
        if i + j <= N:
            dp[i + j] = max(dp[i + j], dp[i] + dp_elem[j])
print(dp[N])
