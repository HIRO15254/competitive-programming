H, W = map(int, input().split(" "))
A = []
sum_c = []
sum_l = [0] * W
for _ in range(H):
    A.append(list(map(int, input().split(" "))))
for i in range(H):
    sum_c.append(sum(A[i]))
    for j in range(W):
        sum_l[j] += A[i][j]
for i in range(H):
    ans_c = [sum_c[i]] * W
    for j in range(W):
        ans_c[j] += sum_l[j]
        ans_c[j] -= A[i][j]
    print(" ".join(map(str, ans_c)))
