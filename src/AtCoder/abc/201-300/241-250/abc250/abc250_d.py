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


def is_ok(p, q, N):
    return p < q and p * (q ** 3) <= N


N = int(input())
prime_ = prime(10 ** 6)
ans = 0
for q in prime_:
    ok = -1
    ng = len(prime_)
    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if is_ok(prime_[mid], q, N):
            ok = mid
        else:
            ng = mid
    ans += ok + 1
print(ans)
