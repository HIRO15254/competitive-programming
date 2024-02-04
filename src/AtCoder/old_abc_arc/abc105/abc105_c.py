N = int(input())
if N == 0:
    print(0)
elif N > 0:
    ans = 0
    i = 0
    while N >= 2 ** i:
        if N >> i & 1:
            if i % 2 == 0:
                ans += 2 ** i
            else:
                ans += 2 ** i + 2 ** (i + 1)
        i += 1
    print(bin(ans)[2:])
else:
    N *= -1
    ans = 0
    i = 0
    while N >= 2 ** i:
        if N >> i & 1:
            if i % 2 != 0:
                ans += 2 ** i
            else:
                ans += 2 ** i + 2 ** (i + 1)
        i += 1
    print(bin(ans)[2:])
