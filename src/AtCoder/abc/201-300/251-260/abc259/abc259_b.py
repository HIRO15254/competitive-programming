import math

a, b, d = map(int, input().split())
ang = math.pi / 180 * d
print(a * math.cos(ang) - b * math.sin(ang), b * math.cos(ang) + a * math.sin(ang))
