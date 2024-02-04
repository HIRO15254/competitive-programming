def gcd(a, b):
    if (a < b):
        q = a
        a = b
        b = q
    while (b > 0):
        r = a % b
        a = b
        b = r
    return a


def prime(max: int):
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


def get_primes(a: int):
    i = 0
    ret = []
    while p[i] ** 2 < a:
        while a % p[i] == 0:
            ret.append(p[i])
            a = a // p[i]
        i += 1
    if a != 1:
        ret.append(a)
    return ret


def solve(A, B):
    mi = min(A, B)
    sa = abs(A - B)
    if sa == 0:
        return 1

    p_sa = get_primes(sa)
    ans = 0
    while sa != 1:
        mi_p = [10 ** 18, -1]
        for i in p_sa:
            if (mi % i) < mi_p[0]:
                mi_p = [mi % i, i]
        ans += mi_p[0]
        p_sa.remove(mi_p[1])
        mi = mi // mi_p[1]
        sa = sa // mi_p[1]
    ans += mi
    return ans


A, B = map(int, input().split())
print(solve(A, B))
