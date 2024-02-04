N = int(input())
s = dict()
for i in range(N):
    sn = input()
    if sn in s:
        s[sn] += 1
    else:
        s[sn] = 1
M = int(input())
for i in range(M):
    tn = input()
    if tn in s:
        s[tn] -= 1
    else:
        s[tn] = -1
ans = 0
for i in s:
    ans = max(ans, s[i])
print(ans)
