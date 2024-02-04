N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))
ans = False
for _ in range(4):
    next_A = []
    for i in range(N):
        next_A.append([])
        for j in range(N):
            next_A[i].append(A[N - j - 1][i])
    A = next_A
    now_ans = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] == 0:
                now_ans = False
    ans = ans or now_ans
if ans:
    print("Yes")
else:
    print("No")
