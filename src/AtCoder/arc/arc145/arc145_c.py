def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 998244353  # 出力の制限
N = int(input())
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

ans = 1
ans_2 = 0
for i in range(N):
    ans *= (N - i) * 2
    ans %= mod
for i in range(N // 2 + 1):
    if i < 2:
        ans_2 += cmb(N - 1, i, mod) ** 2
    else:
        ans_2_ = cmb(N - 1, i, mod) - cmb(N - 3, i - 2, mod)
        while ans_2_ < 0:
            ans_2_ += mod
        ans_2 += ans_2_ ** 2
    ans_2 %= mod
print(ans, ans_2)
ans *= ans_2
ans %= mod
print(ans)
