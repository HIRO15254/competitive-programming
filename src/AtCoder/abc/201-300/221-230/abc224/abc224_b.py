H, W = map(int, input().split(" "))
A = []
for i in range(H):
    A.append(list(map(int, input().split(" "))))
ans = True

for i1 in range(H - 1):
    for i2 in range(i1 + 1, H):
        for j1 in range(W - 1):
            for j2 in range(j1 + 1, W):
                if A[i1][j1] + A[i2][j2] > A[i1][j2] + A[i2][j1]:
                    ans = False

if ans:
    print("Yes")
else:
    print("No")
