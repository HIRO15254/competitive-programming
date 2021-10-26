N = int(input())
yakusu = 0
ans = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        yakusu = 0
        for i2 in range(1, i + 1):
            if i % i2 == 0:
                yakusu += 1
        if yakusu == 8:
            ans += 1
print(ans)
