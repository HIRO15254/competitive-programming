def Meg_nib(ng, border, lists):
    ng = -1
    ok = len(lists) - 1
    if len(lists) == 0 or border >= lists[ok]:
        return -1
    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if lists[mid] > border:
            ok = mid
        else:
            ng = mid
    return lists[ok]


N = input()
S = input()
ans = 0
k = 0
k2 = 0
k3 = 0
find = [[]for _ in range(10)]
for i in range(len(S)):
    find[int(S[i])].append(i)
for i in range(10):
    for i2 in range(10):
        for i3 in range(10):
            k = Meg_nib(0, -1, find[i])
            if k == -1:
                break
            k2 = Meg_nib(0, k, find[i2])
            if k2 == -1:
                break
            k3 = Meg_nib(0, k2, find[i3])
            if k3 != -1:
                ans += 1
print(ans)
