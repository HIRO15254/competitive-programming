N = int(input())
A = list(map(int, input().split(" ")))
ans = -1
swapimos = [0] * N
swap = [0] * (N - 1)
for i in range(N):
    if i > A[i] - 1:
        swapimos[A[i] - 1] += 1
        swapimos[i] -= 1
    else:
        swapimos[A[i] - 1] -= 1
        swapimos[i] += 1
p = 0
if swapimos[0] == 2 and swapimos[-1] == -2:
    swapimos[0] = 0
    swapimos[-1] = 0
    if max(swapimos) == 0 or min(swapimos) == 0:
        ans = 0
    else:
        ans = -1
else:
    ans = -1

if ans != -1:
    c = 0
    ans_l = []
    while c < N - 1:
        i = 0
        while A[c + i] != c + 1:
            i += 1
        for j in range(i):
            ans_l.append(c + i - j)
        c += i
    for i in range(N - 1):
        r = A[ans_l[i]]
        A[ans_l[i]] = A[ans_l[i] - 1]
        A[ans_l[i] - 1] = r
    for i in range(N):
        if A[i] != i + 1:
            ans = -1
    if ans != -1:
        for i in range(N - 1):
            print(ans_l[i])
    else:
        print(-1)

else:
    print(-1)
