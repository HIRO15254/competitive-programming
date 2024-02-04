def prime(max):
    Q = list(range(2, max + 1))
    A = list(range(2, max + 1))
    p = list()
    while A[0] ** 2 < max:
        B = list()
        tmp = A[0]
        p.append(tmp)
        for i in A:
            if i % tmp != 0:
                B.append(i)
            else:
                Q[i - 2] = tmp
        A = B
    p += A
    return p


p = prime(10 ** 6)
p.sort()


def BinarySearch(n):
    ng = len(p) + 1
    ok = -1
    while (abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if p[mid] ** 2 <= n:
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
a = 0
b = 0
c = 0
ans = 0
while p[a] ** 5 <= N:
    b = a + 1
    while p[a] ** 2 * p[b] ** 3 <= N:
        left = N // ((p[a] ** 2) * p[b])
        ans += BinarySearch(left) - b
        b += 1
    a += 1
print(ans)
