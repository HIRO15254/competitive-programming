M, N = map(int, input().rstrip().split(" "))
if N != 0:
    A = set(map(int, input().rstrip().split(" ")))
    ans = -100
    sa = 10 ** 5
    for i in range(-1, 102):
        if i not in A:
            if sa > abs(M - i):
                sa = abs(M - i)
                ans = i
    print(ans)
else:
    print(M)
