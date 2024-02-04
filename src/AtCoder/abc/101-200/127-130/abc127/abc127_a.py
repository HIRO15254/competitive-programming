A, B = map(int, input().rstrip().split(" "))
if A >= 13:
    print(B)
elif A <= 5:
    print(0)
else:
    print(B // 2)
