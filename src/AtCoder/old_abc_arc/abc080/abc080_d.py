N, C = map(int, input().split(" "))
tv = [[]for _ in range(C)]
t_t = [0] * (2 * 10 ** 5 + 10)
for i in range(N):
    s, t, c = map(int, input().split(" "))
    tv[c - 1].append([s, t])
for i in range(C):
    tv[i].sort()
    if len(tv[i]) != 0:
        s, e = tv[i][0]
        for j in range(1, len(tv[i])):
            if tv[i][j][0] != e:
                t_t[s * 2] += 1
                t_t[e * 2 + 1] -= 1
                s = tv[i][j][0]
            e = tv[i][j][1]
        t_t[s * 2] += 1
        t_t[e * 2 + 1] -= 1
now = 0
ans = 0
for i in t_t:
    now += i
    ans = max(ans, now)
print(ans)
