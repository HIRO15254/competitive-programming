a = input().rstrip().split()
A = int(a[0])
B = int(a[1])
if A > B:
    print(str(B) * A)
else:
    print(str(A) * B)
