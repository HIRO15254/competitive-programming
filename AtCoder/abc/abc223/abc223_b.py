S = input()
ans = []
for i in range(len(S)):
    ans.append(S[i:] + S[:i])
ans.sort()
print(ans[0])
print(ans[-1])
