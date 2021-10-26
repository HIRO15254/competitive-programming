A, B = map(int, input().rstrip().split(" "))
e = False
for i in range(10 ** 4):
    if int(i * 0.08) == A and int(i * 0.10) == B:
        print(i)
        e = True
        break
if e is False:
    print(-1)
