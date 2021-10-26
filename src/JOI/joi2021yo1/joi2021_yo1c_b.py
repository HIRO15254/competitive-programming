N = int(input())
S = list(input())
ans = 0
for i in range(N):
    if i % 2 == 0:
        if S[i] != "I":
            ans += 1
    else:
        if S[i] != "O":
            ans += 1
print(ans)
