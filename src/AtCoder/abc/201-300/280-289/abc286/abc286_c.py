N, A, B = map(int, input().split())
S = input()
ans = 10 ** 18
for i in range(N):
    ans_p = A * i
    rep = S[i:] + S[:i]
    for j in range(N // 2):
        if rep[j] != rep[-j - 1]:
            ans_p += B
    ans = min(ans, ans_p)
print(ans)
