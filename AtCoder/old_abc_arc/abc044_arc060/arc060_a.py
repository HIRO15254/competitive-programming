N, A = map(int, input().rstrip().split(" "))
X = list(map(int, input().rstrip().split(" ")))
DPq = [0 for _ in range(1300)]
DPp = [0 for _ in range(1300)]
DPp[0] = 1
DPm = [0 for _ in range(1300)]
DPm[0] = 1
just = 0
ans = 0
for i in X:
    if i > A:
        for i2 in range(1250, -1, -1):
            DPp[i2 + (i - A)] += DPp[i2]
    elif i < A:
        for i2 in range(1250, -1, -1):
            DPm[i2 + (A - i)] += DPm[i2]
    else:
        just += 1
for i in range(1250):
    ans += DPp[i] * DPm[i]
ans *= 2 ** just
ans -= 1
print(ans)
