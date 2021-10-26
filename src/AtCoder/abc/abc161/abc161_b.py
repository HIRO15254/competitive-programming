N, M = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
A.sort()
A.reverse()
if A[M - 1] >= sum(A) / 4 / M:
    print("Yes")
else:
    print("No")
