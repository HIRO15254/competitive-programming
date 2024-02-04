N = int(input())
a = 1
ans = 0
while a ** 3 <= N:
    b = a
    while a * b * b <= N:
        ans += N // (a * b) - (b - 1)
        b += 1
    a += 1
print(ans)
