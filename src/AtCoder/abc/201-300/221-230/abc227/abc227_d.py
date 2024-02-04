N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))


def BinarySearch(ng, ok):
    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


def is_ok(mid):
    counter = 0
    for i in A:
        counter += min(mid, i)
    return counter >= K * mid


print(BinarySearch(10 ** 18, 0))
