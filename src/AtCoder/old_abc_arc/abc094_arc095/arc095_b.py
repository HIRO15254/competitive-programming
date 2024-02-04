N = int(input())
A = list(map(int, input().split()))
A.sort()
ans_1 = A[-1]
A = A[:-1]
ans_2 = A[0]
ans_2_sa = abs(ans_2 - (ans_1 / 2))
for i in A:
    if abs(i - (ans_1 / 2)) < ans_2_sa:
        ans_2 = i
        ans_2_sa = abs(ans_2 - (ans_1 / 2))
print(ans_1, ans_2)