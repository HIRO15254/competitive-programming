N, M = map(int, input().split())
no = [10 ** 9] * N
kiri = 10 ** 18
for i in range(M):
    a, b = map(int, input().split())
    no[a - 1] = min(no[a - 1], b - 1)
ans = 0
for i in range(N):
    if kiri <= i:
        kiri = 10 ** 18
    if no[i] != 10 ** 9:
        if kiri > no[i]:
            if kiri == 10 ** 18:
                ans += 1
            kiri = no[i]
print(ans)
