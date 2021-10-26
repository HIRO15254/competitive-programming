S = list(input())
S.sort()
ans = True
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        ans = False
        break
if ans:
    print("yes")
else:
    print("no")
