N, Q = map(int, input().rstrip().split(" "))
# i = 0:机or空気 その他:箱
desk = [i for i in range(N + 1)]
p = [0 for i in range(N + 1)]
ans = [0 for i in range(N + 1)]
for _ in range(Q):
    f, t, x = map(int, input().rstrip().split(" "))
    q = desk[f]
    desk[f] = p[x]
    p[x] = desk[t]
    desk[t] = q
for i in range(1, N + 1):
    if desk[i] != 0:
        ans[desk[i]] = i
        nex = desk[i]
        while p[nex] != 0:
            ans[p[nex]] = i
            nex = p[nex]
for i in range(1, N + 1):
    print(ans[i])
