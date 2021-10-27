N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
ans = 0
for i in range(Q):
    ma = N
    mi = -1
    B = int(input())
    while (ma - mi) != 1:
        mid = int((ma + mi) / 2)
        if A[mid] < B:
            mi = mid
        else:
            ma = mid
    a = 10 ** 9
    if ma != N:
        a = min(a, abs(B - A[ma]))
    if mi != -1:
        a = min(a, abs(B - A[mi]))
    print(a)
