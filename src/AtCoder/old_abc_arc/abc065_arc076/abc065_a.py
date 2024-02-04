X, A, B = map(int, input().rstrip().split(" "))
if (A >= B):
    print("delicious")
elif(A + X >= B):
    print("safe")
else:
    print("dangerous")
