A = list(map(int, input().rstrip().split(" ")))
A.sort()
if(A[2] == A[0] + A[1]):
    print("Yes")
else:
    print("No")
