N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

price = dict()

for i in range(M):
    price[D[i]] = P[i + 1]

ans = 0
for i in range(N):
    if C[i] in price:
        ans += price[C[i]]
    else:
        ans += P[0]
print(ans)
