N = int(input())
P = list(map(int, input().split()))
dp = dict()
dp[(P[1], )] = 1
ndp = dict()
for i in range(N - 2):
    p = P[i + 2]
    for j, k in dp.items():
        for m in range(len(j)):
            if p > j[m]:
                n = j[:m] + (p, )
                if n in ndp:
                    ndp[n] += k
                else:
                    ndp[n] = k
                ndp[n] %= 998244353
        n = j + (p, )
        if n in ndp:
            ndp[n] += k
        else:
            ndp[n] = k
        ndp[n] %= 998244353
    dp = ndp
    ndp = dict()
ans = 0
for i, j in dp.items():
    ans += j
    ans %= 998244353
print(ans)
