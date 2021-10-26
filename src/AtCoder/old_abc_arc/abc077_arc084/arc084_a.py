N = int(input())
A = list(map(int, input().split(" ")))
A.append(10 ** 18)
A.sort()
B = list(map(int, input().split(" ")))
B.append(10 ** 18)
B_c = [0] * (N + 1)
B.sort()
C = list(map(int, input().split(" ")))
C.sort()
C_c = [0] * N

c = 0
for i in range(N):
    while B[i] > A[c]:
        c += 1
    B_c[i] = c
for i in range(N):
    B_c[i] += B_c[i - 1]
c = 0
for i in range(N):
    while C[i] > B[c]:
        c += 1
    C_c[i] = B_c[c - 1]
print(sum(C_c))
