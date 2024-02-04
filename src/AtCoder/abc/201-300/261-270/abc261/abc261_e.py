N, C = map(int, input().split())
A = [0]
B = [2 ** 30 - 1]
for i in range(N):
    Ti, Ai = map(int, input().split())
    if Ti == 1:
        A.append(A[-1] & Ai)
        B.append(B[-1] & Ai)
    elif Ti == 2:
        A.append(A[-1] | Ai)
        B.append(B[-1] | Ai)
    elif Ti == 3:
        A.append(A[-1] ^ Ai)
        B.append(B[-1] ^ Ai)
now = bin(C)[2:].rjust(30, '0')
for i in range(N):
    ans = 0
    a = bin(A[i + 1])[2:].rjust(30, '0')
    b = bin(B[i + 1])[2:].rjust(30, '0')
    for j in range(30):
        if now[29 - j] == '0':
            ans += (2 ** j if a[29 - j] == '1' else 0)
        else:
            ans += (2 ** j if b[29 - j] == '1' else 0)
    print(ans)
    now = bin(ans)[2:].rjust(30, '0')
