N = int(input())
A = list(map(int, input().rstrip().split(" ")))
A.sort()
lis = []

for i in range(len(A) - 1):
    if A[i] == A[i + 1]:
        lis.append(A[i])
        A[i + 1] = 0
if len(lis) < 2:
    print(0)
else:
    print(lis[-1] * lis[-2])
