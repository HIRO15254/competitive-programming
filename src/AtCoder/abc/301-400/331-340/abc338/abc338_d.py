N, M = map(int, input().split())
X = list(map(int, input().split()))

ans = [0] * N
imos = [0] * N

for i in range(M - 1):
    z_mtg = N - abs(X[i] - X[i + 1])
    not_z_mtg = abs(X[i] - X[i + 1])
    imos[0] += not_z_mtg
    imos[min(X[i], X[i + 1]) - 1] += z_mtg - not_z_mtg
    imos[max(X[i], X[i + 1]) - 1] -= z_mtg - not_z_mtg

ans[0] = imos[0]
for i in range(N - 1):
    ans[i + 1] = ans[i] + imos[i + 1]

print(min(ans))
