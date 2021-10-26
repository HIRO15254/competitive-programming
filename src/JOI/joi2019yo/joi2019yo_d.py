N = int(input())
A = list(map(int, input().split(" ")))
A = [-1] + A + [-1]
s = set()
for i in A:
    s.add(i)
l = list(s)
l.sort()
A2 = []
imos = [0] * (N + 2)


def Meg_nib(q):
    ng = -1
    ok = len(l) - 1
    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if l[mid] >= q:
            ok = mid
        else:
            ng = mid
    return ok


for i in range(N + 2):
    if i == 0 or A[i - 1] != A[i]:
        A2.append(Meg_nib(A[i]))

for i in range(1, len(A2) - 1):
    if max(A2[i - 1], A2[i], A2[i + 1]) == A2[i]:
        imos[A2[i]] -= 1
    if min(A2[i - 1], A2[i], A2[i + 1]) == A2[i]:
        imos[A2[i]] += 1
now = 1
ans = 0
for i in range(N + 2):
    now += imos[i]
    ans = max(now, ans)
if max(A) == 0:
    ans = 0
print(ans)
