import copy
N = int(input())
ans = [0] * N
for i in range(N * (N - 1) // 2):
    A, B, C, D = map(int, input().split(" "))
    if C > D:
        ans[A - 1] += 3
    elif D > C:
        ans[B - 1] += 3
    else:
        ans[A - 1] += 1
        ans[B - 1] += 1
ans_2 = copy.deepcopy(ans)
ans_2.sort(reverse=True)
for i in ans:
    print(ans_2.index(i) + 1)
