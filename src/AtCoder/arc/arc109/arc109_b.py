n = int(input())


def Meg_nib(ng, ok):
    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if mid * (mid + 1) <= (n + 1) * 2:
            ok = mid
        else:
            ng = mid
    return ok


print(n - Meg_nib(10**18, 1) + 1)
