import copy
import time
from collections import deque
import random

start_time = time.time()


def solve(pyram):
    pyramid = copy.deepcopy(pyram)
    min_len = 10 ** 9
    min_ans_len = 0

    def swap(x1, y1, x2, y2):
        ans.append((x1, y1, x2, y2))
        pyramid[x1][y1], pyramid[x2][y2] = pyramid[x2][y2], pyramid[x1][y1]

    def swap_only(x1, y1, x2, y2):
        pyramid[x1][y1], pyramid[x2][y2] = pyramid[x2][y2], pyramid[x1][y1]

    def swap_pyram(x1, y1, x2, y2, py):
        py[x1][y1], py[x2][y2] = py[x2][y2], py[x1][y1]

    ans = []
    ans_len = 0
    for i in range(435):
        for _ in range(29):
            for j in range(29):
                for k in range(j + 1):
                    top = pyramid[j][k]
                    bottom_1 = pyramid[j + 1][k]
                    bottom_2 = pyramid[j + 1][k + 1]
                    if top < bottom_1 and top < bottom_2:
                        continue
                    if top - min(bottom_1, bottom_2) < 435 - i:
                        continue
                    elif bottom_1 < bottom_2:
                        swap(j, k, j + 1, k)
                        ans_len += 1
                    else:
                        swap(j, k, j + 1, k + 1)
                        ans_len += 1
    ans_queue = deque(ans)
    while start_time + 1 > time.time():
        tss = true_solve_step(pyramid)
        # print(ans_len, ans_len + tss)
        if min_len > ans_len + tss:
            min_len = ans_len + tss
            min_ans_len = ans_len
        for i in range(5):
            pop = ans_queue.pop()
            swap_only(pop[0], pop[1], pop[2], pop[3])
            ans_len -= 1

    min_ans = ans[:min_ans_len]
    while start_time + 1.9 > time.time():
        copy_ans = copy.deepcopy(min_ans)
        copy_ans.pop(random.randrange(len(copy_ans)))
        min_ans_len -= 1
        copy_pyram = copy.deepcopy(pyram)
        for i in copy_ans:
            swap_pyram(i[0], i[1], i[2], i[3], copy_pyram)
        tss = true_solve_step(copy_pyram)
        if min_len > min_ans_len + tss:
            min_len = min_ans_len + tss
            min_ans = copy_ans

    for i in min_ans:
        swap_pyram(i[0], i[1], i[2], i[3], pyram)
    return min_ans + true_solve(pyram)


def true_solve(pyramid):
    ans = []

    def swap(x1, y1, x2, y2):
        ans.append((x1, y1, x2, y2))
        pyramid[x1][y1], pyramid[x2][y2] = pyramid[x2][y2], pyramid[x1][y1]

    for i in range(29):
        for j in range(29):
            for k in range(j + 1):
                top = pyramid[j][k]
                bottom_1 = pyramid[j + 1][k]
                bottom_2 = pyramid[j + 1][k + 1]
                if top < bottom_1 and top < bottom_2:
                    continue
                elif bottom_1 < bottom_2:
                    swap(j, k, j + 1, k)
                else:
                    swap(j, k, j + 1, k + 1)
    return ans


def true_solve_step(pyramid):
    pyramid_2 = copy.deepcopy(pyramid)
    ans_len = 0

    def swap(x1, y1, x2, y2):
        pyramid_2[x1][y1], pyramid_2[x2][y2] = pyramid_2[x2][y2], pyramid_2[x1][y1]

    for i in range(29):
        for j in range(29):
            for k in range(j + 1):
                top = pyramid_2[j][k]
                bottom_1 = pyramid_2[j + 1][k]
                bottom_2 = pyramid_2[j + 1][k + 1]
                if top < bottom_1 and top < bottom_2:
                    continue
                elif bottom_1 < bottom_2:
                    swap(j, k, j + 1, k)
                    ans_len += 1
                else:
                    swap(j, k, j + 1, k + 1)
                    ans_len += 1
    return ans_len


pyramid = []
for i in range(30):
    b = list(map(int, input().split()))
    pyramid.append(b)

ans = solve(pyramid)
print(len(ans))
for i in ans:
    print(i[0], i[1], i[2], i[3])
