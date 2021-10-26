N, Q = map(int, input().split())
F = [["N" for _ in range(N)] for _ in range(N)]
que = []
for i in range(Q):
    A = list(map(int, input().split()))
    if A[0] == 1:
        F[A[1] - 1][A[2] - 1] = "Y"
    elif A[0] == 2:
        for i in range(N):
            if F[i][A[1] - 1] == "Y":
                F[A[1] - 1][i] = "Y"
    elif A[0] == 3:
        for i in range(N):
            if F[A[1] - 1][i] == "Y":
                que.append(i)
        for i in que:
            for i2 in range(N):
                if F[i][i2] == "Y":
                    F[A[1] - 1][i2] = "Y"
        que.clear()

for i in range(N):
    F[i][i] = "N"
    print("".join(F[i]))
