x1, y1, x2, y2 = map(int, input().split())
ans = False
for x in range(x1 - 4, x1 + 5):
    for y in range(y1 - 4, y1 + 5):
        ans = ans or ((x - x1) ** 2 + (y - y1) ** 2 == 5 and (x - x2) ** 2 + (y - y2) ** 2 == 5)
if ans:
    print("Yes")
else:
    print("No")
