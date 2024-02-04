N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_s = sorted(A)
B_s = sorted(B)
if A_s != B_s:
    print("No")
else:
    if len(set(A)) != N:
        print("Yes")
    else:
        for i in range(N - 2):
            p = A.index(B[i])
            for j in range(p, i, -1):
                if j == N - 1:
                    A[j - 2], A[j - 1], A[j] = A[j - 1], A[j], A[j - 2]
                else:
                    A[j - 1], A[j], A[j + 1] = A[j], A[j + 1], A[j - 1]
        if A == B:
            print("Yes")
        else:
            print("No")
        