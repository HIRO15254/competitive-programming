S = list(input())
mae = []
ato = []
rev = False
Q = int(input())
for i in range(Q):
    A = list(input().rstrip().split(" "))
    if int(A[0]) == 1:
        if rev:
            rev = False
        else:
            rev = True
    else:
        if (rev and int(A[1]) == 2 or not rev and int(A[1]) == 1):
            mae.append(A[2])
        else:
            ato.append(A[2])
if rev:
    ato.reverse()
    S.reverse()
    print("".join(ato) + "".join(S) + "".join(mae))
else:
    mae.reverse()
    print("".join(mae) + "".join(S) + "".join(ato))
