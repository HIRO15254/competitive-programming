N = int(input())
ans = [0 for i in range(10 ** 4 + 1)]
for i in range(1, 100):
    for i2 in range(1, 100):
        for i3 in range(1, 100):
            k = i**2 + i2 ** 2 + i3 ** 2 + i * i2 + i2 * i3 + i3 * i
            if k <= 10 ** 4:
                ans[k] += 1
for i in range(N):
    print(ans[i + 1])
