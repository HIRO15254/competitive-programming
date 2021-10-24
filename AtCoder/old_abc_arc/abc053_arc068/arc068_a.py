N = int(input())
ans = N // 11 * 2
N %= 11
if N == 0:
    print(ans)
elif N <= 6:
    print(ans + 1)
else:
    print(ans + 2)
