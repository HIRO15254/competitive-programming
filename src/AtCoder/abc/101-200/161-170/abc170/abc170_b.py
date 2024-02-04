A, B = map(int, input().rstrip().split(" "))
if (B % 2 == 0 and A * 2 <= B <= A * 4):
    print("Yes")
else:
    print("No")
