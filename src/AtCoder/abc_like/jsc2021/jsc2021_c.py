A, B = map(int, input().split(" "))
for i in range(B - A, 0, -1):
    k = i - (A % i)
    if k == i:
        k = 0
    if k <= (B - A) - i:
        print(i)
        break
