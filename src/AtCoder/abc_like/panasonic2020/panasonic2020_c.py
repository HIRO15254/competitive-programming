A, B, C = map(int, input().split())
N = C - A - B
if N > 0:
    if A * B * 4 < N ** 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
