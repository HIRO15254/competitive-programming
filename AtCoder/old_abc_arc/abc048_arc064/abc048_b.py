a, b, x = map(int, input().rstrip().split(" "))

p = b // x - a // x
if a % x == 0:
    p += 1
print(p)
