A, B, N = map(int, input().rstrip().split(" "))
x = 0
if B - 1 > N:
    x = N
else:
    x = B - 1
print(int(A * x / B))
