N, C = map(int, input().split(" "))
z_a = []
for i in range(N):
    a, b, c = map(int, input().split(" "))
    z_a.append([a, c])
    z_a.append([b + 1, c * -1])
z_a.sort()
za2 = []
za2.append(z_a[0])
for i in range(N * 2 - 1):
    if za2[-1][0] == z_a[i + 1][0]:
        za2[-1][1] += z_a[i + 1][1]
    else:
        za2.append(z_a[i + 1])
now = 0
ans = 0
for i in range(len(za2) - 1):
    now += za2[i][1]
    ans += (za2[i + 1][0] - za2[i][0]) * min(now, C)
print(ans)
