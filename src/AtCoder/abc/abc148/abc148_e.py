N = int(input())
if N % 2 == 1:
    print(0)
else:
    n = 10
    ans = 0
    while n <= N:
        ans += N // n
        n *= 5
    print(ans)
