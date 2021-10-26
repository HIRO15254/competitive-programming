N = int(input())
X = list(map(int, input().split(" ")))
M = int(input())
A = list(map(int, input().split(" ")))
for i in range(M):
    if not X[A[i] - 1] == 2019 and not X[A[i] - 1] + 1 in X:
        X[A[i] - 1] += 1
for i in X:
    print(i)
