N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
ans = -1

A_c = 0
B_c = 0
while A_c < N and B_c < M:
    if abs(A[A_c] - B[B_c]) <= D:
        ans = max(ans, A[A_c] + B[B_c])
    if A[A_c] + D < B[B_c]:
        B_c += 1
    else:
        A_c += 1

A_c = 0
B_c = 0
while A_c < N and B_c < M:
    if abs(A[A_c] - B[B_c]) <= D:
        ans = max(ans, A[A_c] + B[B_c])
    if A[A_c] < B[B_c] + D:
        A_c += 1
    else:
        B_c += 1
print(ans)
