N = int(input())
points = []
for _ in range(N):
    X, Y = map(int, input().split(" "))
    points.append([X, Y])
op = [[0, 0, False, False, 0]]  # x差分,y差分,x反転,y反転,回転
M = int(input())
for _ in range(M):
    op2 = list(map(int, input().split(" ")))
    if op2[0] == 1:
        op.append([op[-1][1], op[-1][0] * -1, op[-1][3], op[-1][2], op[-1][4] + 1])
    elif op2[0] == 2:
        op.append([op[-1][1] * -1, op[-1][0], op[-1][3], op[-1][2], op[-1][4] - 1])
    elif op2[0] == 3:
        op.append([op[-1][0] * -1 + 2 * op2[1], op[-1][1], not op[-1][2], op[-1][3], op[-1][4]])
    elif op2[0] == 4:
        op.append([op[-1][0], op[-1][1] * -1 + 2 * op2[1], op[-1][2], not op[-1][3], op[-1][4]])
Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split(" "))
    x, y = points[B - 1]
    if op[A][4] % 4 == 1:
        x, y = y, x * -1
    elif op[A][4] % 4 == 2:
        x, y = x * -1, y * -1
    elif op[A][4] % 4 == 3:
        x, y = y * -1, x
    if op[A][2]:
        ansx = op[A][0] - x
    else:
        ansx = op[A][0] + x
    if op[A][3]:
        ansy = op[A][1] - y
    else:
        ansy = op[A][1] + y
    print(ansx, ansy)
