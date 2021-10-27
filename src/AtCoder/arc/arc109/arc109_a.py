a, b, y, x = map(int, input().split(" "))
if (b >= a):
    print(min(y + (b - a) * x, y * (2 * (b - a)) + y))
else:
    print(min(y + (a - b - 1) * x, y * (2 * (a - b)) - y))
