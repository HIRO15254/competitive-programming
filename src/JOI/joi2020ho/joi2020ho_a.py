import copy
N = int(input())
A = list(map(int, input().split(" ")))
P = copy.deepcopy(A)
B = list(map(int, input().split(" ")))
A.sort()
B.sort()
a_dict = dict()
ans = [0 for _ in range(N + 1)]
ans2 = 0
L_ans = []
for i in range(N):
    ans[i] = (max(max(0, A[i] - B[i]), ans[i - 1]))
    a_dict[A[N]] = ans[N - 1]
for i in range(N - 1, -1, -1):
    ans2 = max(ans2, max(0, A[i + 1] - B[i]))
    a_dict[A[i]] = max(ans2, ans[i])

for i in P:
    L_ans.append(a_dict[i])
print(" ".join(map(str, L_ans)))
