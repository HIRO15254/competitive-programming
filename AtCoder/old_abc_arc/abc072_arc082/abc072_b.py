S = list(input())
ans = []
for i in range(1, len(S) + 1, 2):
    ans.append(S[i - 1])
print("".join(ans))
