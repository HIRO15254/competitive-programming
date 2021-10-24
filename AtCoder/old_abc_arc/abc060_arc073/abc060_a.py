A = list(map(str, input().rstrip().split(" ")))
if(A[0][-1] == A[1][0] and A[1][-1] == A[2][0]):
    print("YES")
else:
    print("NO")
