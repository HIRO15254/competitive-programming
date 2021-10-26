r, D, x = map(int, input().rstrip().split(" "))
for i in range(10):
    x = x * r - D
    print(x)
