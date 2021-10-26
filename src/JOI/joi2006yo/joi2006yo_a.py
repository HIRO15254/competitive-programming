N = int(input())
ansa = 0
ansb = 0
for i in range(N):
    A = list(map(int, input().split(" ")))
    if A[0] > A[1]:
        ansa += A[0] + A[1]
    elif A[0] == A[1]:
        ansa += A[0]
        ansb += A[1]
    else:
        ansb += A[0] + A[1]
print(str(ansa) + " " + str(ansb))
