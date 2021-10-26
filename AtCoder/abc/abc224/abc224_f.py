S = input()
N = len(S)

# 10^N (mod 998244353)
TEN_N = [1]
for i in range(N):
    TEN_N.append((TEN_N[-1] * 10) % 998244353)

TWO_N = [1]
for i in range(N):
    TWO_N.append((TWO_N[-1] * 2) % 998244353)
ans = 0

# 現在の倍率
now_m = 0
for i in range(N - 1):
    now_m += TWO_N[N - i - 2] * TEN_N[i]
    now_m %= 998244353
now_m += TEN_N[N - 1]

for i in range(N - 1):
    ans += int(S[i]) * now_m
    ans %= 998244353
    now_m -= (TWO_N[i] * TEN_N[N - 1 - i]) % 998244353
    now_m += (TWO_N[i] * TEN_N[N - 2 - i]) % 998244353
    if now_m < 0:
        now_m += 998244353
ans += int(S[N - 1]) * now_m
ans %= 998244353
print(ans)
