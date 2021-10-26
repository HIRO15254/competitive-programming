N = int(input())
S = list(input())
Q = int(input())
f = False
for _ in range(Q):
    T, A, B = map(int, input().split(" "))
    A = A - 1
    B = B - 1
    if(T == 1):
        if f:
            if A >= N:
                A = A - N
            else:
                A = A + N
            if B >= N:
                B = B - N
            else:
                B = B + N
        S[A], S[B] = S[B], S[A]
    else:
        f = not f
if f:
    print("".join(S[N:]) + "".join(S[:N]))
else:
    print("".join(S))
