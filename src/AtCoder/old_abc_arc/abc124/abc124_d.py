N, K = map(int, input().rstrip().split(" "))
S = list(input())

l = []
ans = 0
q = "1"
n = 0

for i in range(len(S)):
    if q != S[i]:
        l.append(n)
        n = 1
    else:
        n += 1
    q = S[i]
l.append(n)
if S[-1] == "0":
    l.append(0)

maxlen = K * 2 + 1

if maxlen >= len(l):
    print(N)
else:
    su = 0
    for i in range(maxlen):
        su += l[i]
    ans = su
    for i in range(0, len(l) - maxlen, 2):
        su -= l[i] + l[i + 1]
        su += l[maxlen + i] + l[maxlen + i + 1]
        ans = max(ans, su)
    print(ans)
