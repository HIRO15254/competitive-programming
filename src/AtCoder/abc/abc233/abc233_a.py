X, Y = map(int, input().split(" "))
print(max(0, (Y - X - 1) // 10 + 1))
