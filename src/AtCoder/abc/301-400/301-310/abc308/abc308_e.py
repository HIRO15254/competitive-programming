N = int(input())
A = list(map(int, input().split()))
S = input()

dp = [[[0 for _ in range(8)] for _ in range(3)] for _ in range(N + 1)]

dp[0][0][0] = 1

mex_next = [[1, 1, 3, 3, 5, 5, 7, 7], [2, 3, 2, 3, 6, 7, 6, 7], [4, 5, 6, 7, 4, 5, 6, 7]]
mex_ans = [0, 1, 0, 2, 0, 1, 0, 3]

ans = 0
for i in range(N):
    s = "MEX".index(S[i])
    a = A[i]
    for j in range(3):
        for k in range(8):
            dp[i + 1][j][k] += dp[i][j][k]
    if s == 0:
        for j in range(8):
            dp[i + 1][1][mex_next[a][j]] += dp[i][0][j]
    elif s == 1:
        for j in range(8):
            dp[i + 1][2][mex_next[a][j]] += dp[i][1][j]
    else:
        for j in range(8):
            ans += dp[i][s][j] * mex_ans[mex_next[a][j]]
print(ans)
