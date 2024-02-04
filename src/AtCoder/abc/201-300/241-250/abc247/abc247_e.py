N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

XY = [0, -1, -1]
YX = [-1, -1]
r = []
now = [-1, -1]
for i in range(N):
    if A[i] < Y or X < A[i]:
        if now[1] != -1:
            r.append(now)
        elif now[0] != -1 and X == Y:
            r.append([now[0], now[0]])
        now = [-1, -1]
    else:
        if now[0] == -1:
            now[0] = i
        else:
            now[1] = i
if now[1] != -1:
    r.append(now)
elif now[0] != -1 and X == Y:
    r.append([now[0], now[0]])
ans = 0
for i in range(len(r)):
    r_l = r[i][1] - r[i][0] + 1
    if X == Y:
        ans += ((r_l + 1) * r_l) // 2
    else:
        XY = [-1, -1, -1]
        YX = [-1, -1, -1]
        for j in range(r_l):
            if A[r[i][0] + j] == Y:
                if XY[1] == -1:
                    XY[0] = j
                else:
                    XY[2] = j
                    ans += (XY[1] - XY[0]) * (r_l - XY[2])
                    XY[0] = XY[2]
                    XY[1:] = [-1, -1]
                YX[1] = j
            if A[r[i][0] + j] == X:
                if YX[1] == -1:
                    YX[0] = j
                else:
                    YX[2] = j
                    ans += (YX[1] - YX[0]) * (r_l - YX[2])
                    YX[0] = YX[2]
                    YX[1:] = [-1, -1]
                XY[1] = j
print(ans)
