A, B = map(int, input().rstrip().split(" "))
print(max(A + B, A * 2 - 1, B * 2 - 1))
