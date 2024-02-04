N, M, T = map(int, input().split())
A = list(map(int, input().split()))
BONUS = [0] * N
for _ in range(M):
    X, Y = map(int, input().split())
    BONUS[X - 1] = Y
for i in range(N - 1):
    T += BONUS[i]
    T -= A[i]
    if T <= 0:
        print("No")
        break
else:
    print("Yes")
