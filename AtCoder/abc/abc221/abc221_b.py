S = input()
T = input()
ans = 0
i = 0
while i < len(S) - 1:
    if S[i] != T[i]:
        if S[i + 1] == T[i] and S[i] == T[i + 1]:
            ans += 1
        else:
            ans += 2
        i += 1
    i += 1
if ans <= 1:
    print("Yes")
else:
    print("No")
