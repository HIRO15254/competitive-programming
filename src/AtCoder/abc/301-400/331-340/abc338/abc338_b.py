S = input()
alp = "abcdefghijklmnopqrstuvwxyz"
ans = []
for i in range(len(alp)):
    ans.append(S.count(alp[i]))
for i in range(len(alp)):
    if ans[i] == max(ans):
        print(alp[i])
        break
