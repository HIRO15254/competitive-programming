X = list(map(int, list(input())))
M = int(input())


def isok(n):
    k = 0
    y = 1
    for i in range(len(X)):
        k += y * X[-1 * (i + 1)]
        y *= n
    return k <= M


if len(X) == 1:
    if X[0] <= M:
        print(1)
    else:
        print(0)
else:
    ok = -1
    ng = 10 ** 18 + 10
    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if isok(mid):
            ok = mid
        else:
            ng = mid
    print(max(0, ok - max(X)))
