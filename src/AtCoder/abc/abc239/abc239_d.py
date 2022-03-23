def prime(max):
    Q = list(range(2, max + 1))
    A = list(range(2, max + 1))
    p = list()
    while A[0] ** 2 < max:
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
    return p

p = set(prime(200))
A, B, C, D = map(int, input().split())
ans = False
for t in range(A, B + 1):
    ans_2 = True
    for a in range(C, D + 1):
        ans_2 = ans_2 and not((t + a) in p)
    ans = ans or ans_2
if ans:
    print("Takahashi")
else:
    print("Aoki")
