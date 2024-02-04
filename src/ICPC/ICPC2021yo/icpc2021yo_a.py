while True:
    A = list(map(int, input().split()))
    if sum(A) == 0:
        break
    while sum(A) != max(A):
        mined = False
        i = 0
        while i < len(A):
            if A[i] == 0:
                A.pop(i)
            else:
                i += 1
        minA = min(A)
        for i in range(len(A)):
            if A[i] != minA or mined:
                A[i] -= minA
            else:
                mined = True
    print(max(A))
