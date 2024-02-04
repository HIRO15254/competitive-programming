N, K = map(int, input().rstrip().split(" "))
p = list(map(int, input().rstrip().split(" ")))
karians = K
for i in range(K):
    karians += p[i]
ans = karians
for i in range(N - K):
    karians -= p[i]
    karians += p[i + K]
    if ans < karians:
        ans = karians
print(ans / 2)
