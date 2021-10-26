N = int(input())
Balls = []
for i in range(N):
    X, C = map(int, input().split(" "))
    Balls.append([C, X])
Balls.sort()
Poses = []
now_color = Balls[0][0]
ma = -10**18
mi = 10**18
for i in Balls:
    if i[0] == now_color:
        ma = max(ma, i[1])
        mi = min(mi, i[1])
    else:
        Poses.append([mi, ma])
        now_color = i[0]
        ma = i[1]
        mi = i[1]
Poses.append([mi, ma])
DP = [[0, 0] for _ in range(len(Poses) + 1)]
DP[0][0] = abs(Poses[0][0]) + abs(Poses[0][0] - Poses[0][1])
DP[0][1] = abs(Poses[0][1]) + abs(Poses[0][0] - Poses[0][1])
for i in range(0, len(Poses) - 1):
    DP[i + 1][0] = min(DP[i][0] + abs(Poses[i][1] - Poses[i + 1][0]), DP[i][1] + abs(Poses[i][0] - Poses[i + 1][0])) + abs(Poses[i + 1][0] - Poses[i + 1][1])
    DP[i + 1][1] = min(DP[i][0] + abs(Poses[i][1] - Poses[i + 1][1]), DP[i][1] + abs(Poses[i][0] - Poses[i + 1][1])) + abs(Poses[i + 1][0] - Poses[i + 1][1])
DP[-1][0] = DP[-2][0] + abs(Poses[-1][1])
DP[-1][1] = DP[-2][1] + abs(Poses[-1][0])
print(min(DP[len(Poses)]))
