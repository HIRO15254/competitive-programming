W, a, b = map(int, input().rstrip().split(" "))
if abs(a - b) <= W:
    print(0)
else:
    print(abs(a - b) - W)
