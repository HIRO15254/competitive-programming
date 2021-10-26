H, W = map(int, input().split(" "))
ans = 10 ** 10
karians = [0, 0, 0]
if H % 3 == 0 or W % 3 == 0:
    ans = 0
k = int(W / 2)
for i in range(H + 1):
    karians = [i * W, k * (H - i), (W - k) * (H - i)]
    karians.sort()
    if (karians[2] - karians[0] < ans):
        ans = karians[2] - karians[0]
k = int(H / 2)
for i in range(W + 1):
    karians = [i * H, k * (W - i), (H - k) * (W - i)]
    karians.sort()
    if (karians[2] - karians[0] < ans):
        ans = karians[2] - karians[0]
if(W < ans):
    ans = W
if(H < ans):
    ans = H

print(ans)
