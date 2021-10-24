D = [i for i in range(10)]
N, K = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
flag = True
for i in range(N, 10 ** 6 + 1):
    flag = True
    for i2 in range(6):
        if i >= 10 ** i2 and (i // (10 ** i2)) % 10 in A:
            flag = False
            break
    if flag:
        print(i)
        break
