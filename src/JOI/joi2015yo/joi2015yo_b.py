N = int(input())
M = int(input())
point = [0] * N
A = list(map(int, input().split(" ")))
for i in range(M):
    K = list(map(int, input().split(" ")))
    for j in range(N):
        if K[j] == A[i]:
            point[j] += 1
        else:
            point[A[i] - 1] += 1
for i in range(N):
    print(point[i])
