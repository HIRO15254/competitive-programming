from collections import deque

W, H, N = map(int, input().split())
points = []
for i in range(N * 2):
    x, y, c = map(int, input().split())
    z = 0
    if y == 0:
        z = x
    elif x == W:
        z = W + y
    elif y == H:
        z = W + H + (W - x)
    else:
        z = W + H + W + (H - y)
    points.append([z, c])
points.sort()
stack = deque()
ans = True
for i in range(N):
    col_val = []
    for j in range(2 * N):
        if points[j][1] == i + 1:
            col_val.append(points[j][0])
    col_in = set()
    col_not_in = set()
    for j in range(2 * N):
        if points[j][1] != i + 1:
            if col_val[0] <= points[j][0] and points[j][0] <= col_val[1]:
                if points[j][1] in col_not_in:
                    ans = False
                    break
                col_in.add(points[j][1])
            else:
                if points[j][1] in col_in:
                    ans = False
                    break
                col_not_in.add(points[j][1])
if ans:
    print("Yes")
else:
    print("No")
