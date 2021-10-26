N, M, K = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
B = list(map(int, input().rstrip().split(" ")))
A.append(10 ** 10)
B.append(10 ** 10)
Ai = 0
ans = 0
karians = 0
Aii = 0
Bii = 0
for i in range(N + 1):
    Ai += A[i]
    if Ai > K:
        Ai -= A[i]
        karians = i
        Aii = i
        ans = i
        break
for i in range(Aii + 1):
    while Ai <= K:
        Ai += B[Bii]
        karians += 1
        Bii += 1
    karians -= 1
    Bii -= 1
    Ai -= B[Bii]
    if karians > ans:
        ans = karians
    Ai -= A[Aii - 1 - i]
    karians -= 1
print(ans)
