N = int(input())
S = list(input())

ans = 0
for i in range(N + 1):
    Sl = set(S[:i])
    Sr = set(S[i:])
    ans_s = 0
    for j in Sl:
        if j in Sr:
            ans_s += 1
    ans = max(ans, ans_s)
print(ans)
