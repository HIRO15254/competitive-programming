r = 10 ** 9
r2 = 0
s = 0
for _ in range(4):
    p = int(input())
    r = min(r, p)
    r2 += p
for _ in range(2):
    s = max(int(input()), s)
print(r2 - r + s)
