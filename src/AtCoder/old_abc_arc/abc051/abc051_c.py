sx, sy, tx, ty = map(int, input().rstrip().split(" "))
dx = tx - sx
dy = ty - sy
ans = ""
ans += "R" * dx + "U" * dy
ans += "L" * dx + "D" * dy
ans += "D" + "R" * (dx + 1) + "U" * (dy + 1) + "L"
ans += "U" + "L" * (dx + 1) + "D" * (dy + 1) + "R"
print(ans)
