N = int(input())
A = [0] * (N + 1)
B = [0] * (N + 1)
for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        A[i + 1] = P
    else:
        B[i + 1] = P
for i in range(1, N + 1):
    A[i] += A[i - 1]
    B[i] += B[i - 1]
Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    print(A[R] - A[L - 1], B[R] - B[L - 1])
