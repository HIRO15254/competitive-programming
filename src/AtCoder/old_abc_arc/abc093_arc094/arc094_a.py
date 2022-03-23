A = list(map(int, input().split()))
A.sort()
if sum(A) % 2 == 0:
    print(((A[2] + A[2] % 2) * 3 - sum(A)) // 2)
else:
    print(((A[2] + (1 - A[2] % 2)) * 3 - sum(A)) // 2)
