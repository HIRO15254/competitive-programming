N = int(input())
K = list(map(int, input().rstrip().split()))
CK = [0 for _ in range(N + 1)]
ans = 0
for i in K:
    CK[i] += 1
for i in range(N + 1):
    ans += CK[i] * (CK[i] - 1) / 2
for i in range(N):
    bans = ans - CK[K[i]] * (CK[K[i]] - 1) / 2 + (CK[K[i]] - 1) * (CK[K[i]] - 2) / 2
    print(int(bans))
