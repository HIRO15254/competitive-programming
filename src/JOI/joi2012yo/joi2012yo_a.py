p = 10 ** 9
j = 10 ** 9
for _ in range(3):
    p = min(int(input()), p)
for _ in range(2):
    j = min(int(input()), j)
print(p + j - 50)
