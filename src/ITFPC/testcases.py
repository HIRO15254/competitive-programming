from random import randint, shuffle
from collections import deque

for case_no in range(1, 11):
    W = randint(1, 100)
    H = randint(1, 100)
    N = randint(1, min(50, H + W))
    points = set()
    while len(points) < 2 * N:
        points.add(randint(1, W + H * 2))
    new_points = list(points)
    new_points.sort()
    ans = randint(1, 2)
    points_colors = []
    if ans == 1:
        colors = list(range(1, N + 1))
        shuffle(colors)
        color_now = 0
        stack = deque()
        for i in range(2 * N):
            ty = randint(1, 2)
            if (ty == 1 or len(stack) == 0) and color_now != N:
                stack.append(colors[color_now])
                points_colors.append(colors[color_now])
                color_now += 1
            else:
                points_colors.append(stack.pop())
    else:
        points_colors = list(range(1, N + 1)) + list(range(1, N + 1))
        shuffle(points_colors)
        test_stack = deque()
        for i in range(2 * N):
            if len(test_stack) == 0:
                test_stack.append(points_colors[i])
            elif test_stack[-1] == points_colors[i]:
                test_stack.pop()
            else:
                test_stack.append(points_colors[i])
        if len(test_stack) == 0:
            print("偶然にも正解が生成されました。")
            ans = 1
    testcase = []
    for i in range(2 * N):
        if new_points[i] <= W:
            testcase.append([new_points[i], 0, points_colors[i]])
        elif new_points[i] <= W + H:
            testcase.append([W, new_points[i] - W, points_colors[i]])
        elif new_points[i] <= W + H + W:
            testcase.append([W - (new_points[i] - W - H), H, points_colors[i]])
        else:
            testcase.append([0, H - (new_points[i] - W - H - W), points_colors[i]])
    print(case_no, W, H, N, ans)
    shuffle(testcase)
    f = open(f'input/small_{case_no}.txt', 'w')
    f.write(" ".join(map(str, [W, H, N])) + "\n")
    for i in testcase:
        f.write(" ".join(map(str, i)) + "\n")
    f.close()
    f = open(f'output/small_{case_no}.txt', 'w')
    f.write("Yes" if ans == 1 else "No" + "\n")
    f.close()
