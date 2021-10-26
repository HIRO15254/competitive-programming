N = int(input()) + 1000
Q = list(range(2, N + 1))
A = list(range(2, N + 1))
p = list()
while A[0] ** 2 < N:
    B = list()
    tmp = A[0]
    p.append(tmp)
    for i in A:
        if i % tmp != 0:
            B.append(i)
        else:
            Q[i - 2] = tmp
    A = B
p += A

for i in p:
    if i >= N - 1000:
        print(i)
        break
