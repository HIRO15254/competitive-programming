alp = "abcdefghijklmnopqrstuvwxyz"
ans = [False for _ in range(26)]
S = list(input())
for i in S:
    for p in range(26):
        if i == alp[p]:
            ans[p] = True
for i in range(26):
    if ans[i] is False:
        print(alp[i])
        break
else:
    print("None")
