def nib(B, A):
    ng = len(B)
    ok = 0
    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if B[mid] > A:
            ok = mid
        else:
            ng = mid
    return ok + 1


N = int(input())
A = []
B = []
for i in range(N):
    p = int(input())
    A.append(p)
    B.append(p)
B.append(10000)
B.sort(reverse=True)
for i in A:
    print(nib(B, i))
