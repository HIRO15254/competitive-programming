N, M, K = map(int, input().split())
DP = [1] * M
if K == 0:
    ans = 1
    for i in range(N):
        ans *= M
        ans %= 998244353
    print(ans)
else:
    for i in range(N - 1):
        syaku = [0] * (M + 1)
        for j in range(M):
            if j - K + 1 > 0:
                syaku[0] += DP[j]
                syaku[j - K + 1] -= DP[j]
            if j + K < M:
                syaku[j + K] += DP[j]
                syaku[M] -= DP[j]
        now = syaku[0]
        new_DP = []
        for i in range(M):
            new_DP.append(now % 998244353)
            now += syaku[i + 1]
        DP = new_DP
    print(sum(new_DP) % 998244353)
