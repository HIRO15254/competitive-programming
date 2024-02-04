poly = [[[[".", ".", ".", "."] for _ in range(4)] for _ in range(4)] for _ in range(3)]
for i in range(3):
    for j in range(4):
        inp = list(input())
        poly[i][0][j] = inp
        for k in range(4):
            poly[i][1][k][3 - j] = inp[k]
        poly[i][2][3 - j] = inp[::-1]
        for k in range(4):
            poly[i][3][3 - k][j] = inp[k]
check = 0
for i in range(3):
    for j in range(4):
        check += poly[i][0][j].count("#")
if check != 16:
    print("No")
    exit()

x_max = [[3 for _ in range(4)] for _ in range(3)]
y_max = [[3 for _ in range(4)] for _ in range(3)]
x_min = [[-3 for _ in range(4)] for _ in range(3)]
y_min = [[-3 for _ in range(4)] for _ in range(3)]
for i in range(3):
    for j in range(4):
        for x in range(4):
            for y in range(4):
                if poly[i][j][x][y] == "#":
                    x_max[i][j] = min(x_max[i][j], 3 - x)
                    y_max[i][j] = min(y_max[i][j], 3 - y)
                    x_min[i][j] = max(x_min[i][j], -x)
                    y_min[i][j] = max(y_min[i][j], -y)
for muki_1 in range(4):
    for x_1 in range(x_min[0][muki_1], x_max[0][muki_1] + 1):
        for y_1 in range(y_min[0][muki_1], y_max[0][muki_1] + 1):
            for muki_2 in range(4):
                for x_2 in range(x_min[1][muki_2], x_max[1][muki_2] + 1):
                    for y_2 in range(y_min[1][muki_2], y_max[1][muki_2] + 1):
                        for muki_3 in range(4):
                            for x_3 in range(x_min[2][muki_3], x_max[2][muki_3] + 1):
                                for y_3 in range(y_min[2][muki_3], y_max[2][muki_3] + 1):
                                    ans = [[".", ".", ".", "."] for _ in range(4)]
                                    for i in range(4):
                                        for j in range(4):
                                            if 0 <= i - x_1 and i - x_1 < 4 and 0 <= j - y_1 and j - y_1 < 4:
                                                if poly[0][muki_1][i - x_1][j - y_1] == "#":
                                                    ans[i][j] = "#"
                                    for i in range(4):
                                        for j in range(4):
                                            if 0 <= i - x_2 and i - x_2 < 4 and 0 <= j - y_2 and j - y_2 < 4:
                                                if poly[1][muki_2][i - x_2][j - y_2] == "#":
                                                    ans[i][j] = "#"
                                    for i in range(4):
                                        for j in range(4):
                                            if 0 <= i - x_3 and i - x_3 < 4 and 0 <= j - y_3 and j - y_3 < 4:
                                                if poly[2][muki_3][i - x_3][j - y_3] == "#":
                                                    ans[i][j] = "#"
                                    if ans == [["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"]]:
                                        print("Yes")
                                        exit()
print("No")
