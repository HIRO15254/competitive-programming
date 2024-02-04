N, Q = map(int, input().split())

ans = N
p = list(range(N))
e = [[[], 0] for _ in range(N)]

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        q[1] -= 1
        q[2] -= 1
        if e[p[q[1]]][1] == 0:
            ans -= 1
        if e[p[q[2]]][1] == 0:
            ans -= 1
        e[p[q[1]]][0].append(p[q[2]])
        e[p[q[2]]][0].append(p[q[1]])
        e[p[q[1]]][1] += 1
        e[p[q[2]]][1] += 1
    if q[0] == 2:
        q[1] -= 1
        if e[p[q[1]]][1] != 0:
            ans += 1
            for j in e[p[q[1]]][0]:
                e[j][1] -= 1
                if e[j][1] == 0:
                    ans += 1
        e[p[q[1]]][1] = -1
        e.append([[], 0])
        p[q[1]] = len(e) - 1
    # print(p, e)
    print(ans)
