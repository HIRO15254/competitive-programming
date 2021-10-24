A = input()
B = input()
if len(A) > len(B):
    print("GREATER")
elif len(B) > len(A):
    print("LESS")
else:
    for i in range(len(A)):
        if int(A[i]) > int(B[i]):
            print("GREATER")
            break
        elif int(A[i]) < int(B[i]):
            print("LESS")
            break
        if i == len(A) - 1:
            print("EQUAL")
