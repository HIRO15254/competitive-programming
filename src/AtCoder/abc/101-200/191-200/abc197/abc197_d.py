import math
N = int(input())
x0, y0 = map(int, input().split(" "))
xn, yn = map(int, input().split(" "))
xc = (x0 + xn) / 2
yc = (y0 + yn) / 2
xd = math.cos(math.pi / (N / 2))
yd = math.sin(math.pi / (N / 2))
xe = x0 - xc
ye = y0 - yc
print(xe * xd - ye * yd + xc, xe * yd + ye * xd + yc)
