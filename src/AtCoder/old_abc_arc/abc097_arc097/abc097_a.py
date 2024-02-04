a, b, c, d = map(int, input().split())
ans = abs(a - c) <= d or (abs(a - b) <= d and abs(b - c) <= d)
if ans:
    print("Yes")
else:
    print("No")