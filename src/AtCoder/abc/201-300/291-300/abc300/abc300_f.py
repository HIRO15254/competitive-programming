N, M, K = map(int, input().split())
S = list(input())
x_loop = S.count("x")
ans_min = max((K // x_loop) - 1, 0)
K_2 = K - (x_loop * ans_min)

S_int_f = []
S_int_b = []

c = 0
for i in S:
    if i == "x":
        c += 1
    S_int_f.append(c)
c = 0
for i in S[::-1]:
    if i == "x":
        c += 1
    S_int_b.append(c)


def s_f(n):
    mi = -1
    ma = N
    while (abs(ma - mi) > 1):
        mid = (mi + ma) // 2
        if (S_int_f[mid] <= n):
            mi = mid
        else:
            ma = mid
    return mi + 1


def s_b(n):
    mi = -1
    ma = N
    while (abs(ma - mi) > 1):
        mid = (mi + ma) // 2
        if (S_int_b[mid] <= n):
            mi = mid
        else:
            ma = mid
    return mi + 1


ans = 0
if (K <= x_loop):
    ans = s_f(K)
    for i in range(N):
        ans = max(ans, s_f(K + S_int_f[i]) - (i + 1))
if (M >= 2):
    for i in range(K_2 + 1):
        ans = max(ans, s_f(i) + s_b(K_2 - i))
    if (K_2 >= x_loop and ans_min < M - 2):
        for i in range(K_2 - x_loop + 1):
            ans = max(ans, s_f(i) + s_b(K_2 - x_loop - i) + N)
print(ans + ans_min * N)
