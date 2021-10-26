A, B, C = map(int, input().rstrip().split(" "))
print(A + B + C - min(A, min(B, C)))
