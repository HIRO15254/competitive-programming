import heapq

N, M = map(int, input().split())
P = list(map(int, input().split())) + [10 ** 18]
L = list(map(int, input().split()))
D = list(map(int, input().split()))

coupons = []
for i in range(M):
    coupons.append([L[i], -D[i]])
coupons.append([10 ** 18, 0])

coupons.sort()
P.sort()
ans = sum(P[:N])

coupon_list = []
coupon_now = 0

for i in range(N):
    P_max = P[i]
    while coupons[coupon_now][0] <= P_max:
        heapq.heappush(coupon_list, coupons[coupon_now][1])
        coupon_now += 1
    if len(coupon_list) > 0:
        ans += heapq.heappop(coupon_list)
print(ans)
