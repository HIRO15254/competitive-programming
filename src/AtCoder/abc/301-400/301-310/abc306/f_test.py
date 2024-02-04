print(10 ** 4, 10 ** 2)
for i in range((10 ** 4) // 10):
    ans = list(range(10 ** 2 * i, 10 ** 2 * (i + 1)))
    print(" ".join(map(str, ans)))
