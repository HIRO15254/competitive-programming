_ = input()
A = list(map(int, input().rstrip().split(" ")))
ans = [0, 0]
q = [0 for _ in range(9)]
for i in A:
    q[min(8, i // 400)] += 1
for i in range(9):
    if i == 8:
        ans[1] += q[i]
    else:
        if q[i] != 0:
            ans[0] += 1
            ans[1] += 1
ans[0] = max(1, ans[0])
print(str(ans[0]) + " " + str(ans[1]))
