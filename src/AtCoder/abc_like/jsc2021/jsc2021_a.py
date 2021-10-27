X, Y, Z = map(int, input().split(" "))
i = 1
while i * X < Y * Z:
    i += 1
print(i - 1)
