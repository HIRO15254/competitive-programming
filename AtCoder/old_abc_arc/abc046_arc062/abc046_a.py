A = list(map(int, input().rstrip().split(" ")))
A.sort()
if A[0] == A[1]:
    if A[1] == A[2]:
        print(1)
    else:
        print(2)
else:
    if A[1] == A[2]:
        print(2)
    else:
        print(3)
