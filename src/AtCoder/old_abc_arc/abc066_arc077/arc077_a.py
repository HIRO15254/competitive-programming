n = int(input())
a = list(map(int, input().rstrip().split(" ")))
b1 = []
b2 = []
ans = []
if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            b1.append(a[i])
        else:
            b2.append(a[i])
    b2.reverse()
    ans = b2 + b1
    print(" ".join(str(i) for i in ans))
else:
    for i in range(n):
        if i % 2 == 0:
            b1.append(a[i])
        else:
            b2.append(a[i])
    b1.reverse()
    ans = b1 + b2
    print(" ".join(str(i) for i in ans))
