N, M = map(int, input().split())
ans = [1, 0]
for i in range(N - 1):
    old_ans = ans[1]
    ans[1] = ans[0] * (M - 1) + ans[1] * (M - 2)
    ans[0] = old_ans
    ans[0] %= 998244353
    ans[1] %= 998244353
last_ans = ans[1] * M
last_ans %= 998244353
print(last_ans)
