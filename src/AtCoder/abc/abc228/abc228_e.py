def pow_mod(a, b, q):
    """aのb乗(mod q) をlogNで求めます"""
    po = [a]
    p = 1
    while p <= b:
        po.append((po[-1] ** 2) % q)
        p *= 2
    ans = 1
    for i in range(len(po)):  # このループが一番のポイント
        if ((b >> i) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            ans *= po[i]
            ans %= q
    return ans


N, K, M = map(int, input().split(" "))
ans = pow_mod(K, N, 998244352)
if ans == 0:
    ans = 998244352
ans = pow_mod(M, ans, 998244353)
print(ans)
