x, a, b = map(int, input().rstrip().split(" "))
if abs(x - a) < abs(x - b):
    print("A")
else:
    print("B")
