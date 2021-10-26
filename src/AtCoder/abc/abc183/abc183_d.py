N, W = map(int, input().split(" "))
imos = [0 for _ in range(2 * 10 ** 5 + 1)]
for _ in range(N):
    S, T, P = map(int, input().split(" "))
    imos[S] += P
    imos[T] -= P
now = 0
nowmax = 0
for i in range(2 * 10 ** 5 + 1):
    now += imos[i]
    nowmax = max(nowmax, now)
if nowmax <= W:
    print("Yes")
else:
    print("No")
