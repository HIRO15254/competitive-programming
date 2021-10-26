_ = input()
A = list(map(int, input().rstrip().split(" ")))
B = list(map(int, input().rstrip().split(" ")))
C = A + B
C.sort()
for i in C:
    print(i)
