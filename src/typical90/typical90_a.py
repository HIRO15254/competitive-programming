N, L = map(int, input().split(" "))
K = int(input())
A = list(map(int, input().split(" "))) + [L]


def can_split(lim):
    k = 0
    c = 0
    for i in A:
        if i - k >= lim:
            c += 1
            k = i
    return c > K


ng = 10**9
ok = 0
while(abs(ng - ok) > 1):
    mid = (ok + ng) // 2
    if can_split(mid):
        ok = mid
    else:
        ng = mid
print(ok)
