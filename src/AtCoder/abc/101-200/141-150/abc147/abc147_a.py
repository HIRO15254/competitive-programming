A = list(map(int, input().rstrip().split()))
if A[0] + A[1] + A[2] <= 21:
    print("win")
else:
    print("bust")
