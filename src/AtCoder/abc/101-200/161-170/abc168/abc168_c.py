import math
A, B, H, M = map(int, input().rstrip().split(" "))
pi = math.pi
ans = 0
a_x = math.cos((H * 60 + M) / 360 * pi) * A
a_y = math.sin((H * 60 + M) / 360 * pi) * A
b_x = math.cos(M / 30 * pi) * B
b_y = math.sin(M / 30 * pi) * B
ans = math.sqrt(abs(a_x - b_x) ** 2 + abs(a_y - b_y) ** 2)
print(ans)
