N, K = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
for i in range(K, N):
    if (A[i - K] < A[i]):
        print("Yes")
    else:
        print("No")
