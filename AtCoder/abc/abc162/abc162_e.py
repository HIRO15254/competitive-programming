def modpow(a, n, mod):
    bi = str(format(n, "b"))
    res = 1
    for i in range(len(bi)):
        res = (res * res) % mod
        if bi[i] == "1":
            res = (res * a) % mod
    return res


def div(N):
    divv = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            divv.append(i)
            if i != N // i:
                divv.append(N // i)
    return(divv)


N, K = map(int, input().rstrip().split())
O = []
p = [0 for i in range(K + 1)]
ans = 0
for i in range(K, 0, -1):
    p[i] = modpow(int(K / i), N, 1000000007)
for i in range(K, 0, -1):
    ans = (ans + (p[i] * i)) % 1000000007
    O = div(i)
    for o in O:
        if o != i:
            p[o] -= p[i]
print(ans)
