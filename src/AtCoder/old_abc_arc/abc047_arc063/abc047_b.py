W, H, N = map(int, input().rstrip().split(" "))
T = 0
B = H
R = W
L = 0
for i in range(N):
    x, y, a = map(int, input().rstrip().split(" "))
    if a == 1:
        L = max(L, x)
    elif a == 2:
        R = min(R, x)
    elif a == 3:
        T = max(T, y)
    elif a == 4:
        B = min(B, y)
print(max((B - T), 0) * max((R - L), 0))
