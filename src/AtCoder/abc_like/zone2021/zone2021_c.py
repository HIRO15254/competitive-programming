N = int(input())
mem = []
for i in range(N):
    mem.append(list(map(int, input().split(" "))))


def is_ok(ans):
    DP = [[False] * (2**5) for _ in range(3)]
    for i in range(N):
        p = 0
        for j in range(5):
            if(mem[i][j] >= ans):
                p += 2 ** j
        DP[0][p] = True
        for j in range(2):
            for k in range(32):
                if DP[j][k]:
                    DP[j + 1][k | p] = True
    return DP[2][31]


ng = 2 * (10 ** 9)
ok = 0
while(abs(ng - ok) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
