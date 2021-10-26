N = int(input())
s = []
ans = []
flag = True
flag2 = False
for i in range(N):
    s.append(set(input()))
for i in range(N // 2):
    flag2 = False
    for i2 in s[i]:
        if i2 in s[len(s) - 1 - i]:
            ans.append(i2)
            flag2 = True
            break
    if not flag2:
        print(-1)
        flag = False
        break
if N % 2 == 1:
    ans.append(s[(N - 1) // 2].pop())
if flag:
    for i in range(N // 2):
        ans.append(ans[N // 2 - i - 1])
    print("".join(ans))
