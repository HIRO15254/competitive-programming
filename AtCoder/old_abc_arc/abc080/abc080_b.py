N = int(input())
N2 = N
fN = 0
while N2 > 0:
    fN += N2 % 10
    N2 = N2 // 10
if N % fN == 0:
    print("Yes")
else:
    print("No")
