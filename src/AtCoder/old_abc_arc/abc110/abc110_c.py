s1 = input()
s2 = input()
N = len(s1)
s1l = []
s2l = []
ans = True
f = False
for i in range(N):
    f = True
    for s in range(len(s1l)):
        if s1[i] == s1l[s]:
            if s2[i] != s2l[s]:
                ans = False
            f = False
            break
        elif s2[i] == s2l[s]:
            ans = False
    if f:
        s1l.append(s1[i])
        s2l.append(s2[i])
if ans:
    print("Yes")
else:
    print("No")
