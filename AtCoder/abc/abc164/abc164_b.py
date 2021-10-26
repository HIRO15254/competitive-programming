A, B, C, D = map(int, input().rstrip().split(" "))
for i in range(100):
    C -= B
    if (C <= 0):
        print("Yes")
        break
    A -= D
    if (A <= 0):
        print("No")
        break
