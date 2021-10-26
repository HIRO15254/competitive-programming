

def is_ok(mid, K, A):
    p = 0
    for i in A:
        p += (i - 1) // mid
    if p > K:
        return False
    else:
        return True


N, K = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
A.sort()
maxi = A[0]

ng = 0
ok = 10 ** 9
while(abs(ng - ok) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid, K, A):
        ok = mid
    else:
        ng = mid
print(ok)
