S = list(input())
ans = 0
ans2 = 0
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "0":
            ans += 1
    else:
        if S[i] == "1":
            ans += 1

for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "1":
            ans2 += 1
    else:
        if S[i] == "0":
            ans2 += 1

print(min(ans, ans2))
