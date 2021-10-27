P, N = map(int, input().split(" "))
n = [N - 2]
ans = N - 1
i = 1
while 2 ** i <= P - 1:
    n.append((n[-1] ** 2) % (10 ** 9 + 7))
    i += 1
i = 0
while 2 ** i <= P - 1:
    if ((P - 1) >> i) & 1:
        ans *= n[i]
        ans %= 10 ** 9 + 7
    i += 1
print(ans)
