N, M = map(int, input().rstrip().split(" "))
A = []
B = []
ans = False
for i in range(N):
    A.append(list(input()))
for i in range(M):
    B.append(list(input()))
for i in range(N - M + 1):
    for i2 in range(N - M + 1):
        for i3 in range(M):
            if A[i3 + i][i2:i2 + M] != B[i3]:
                break
            if i3 == M - 1:
                ans = True
if ans:
    print("Yes")
else:
    print("No")
