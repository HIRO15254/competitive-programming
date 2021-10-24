N = int(input())
A = list(map(int, input().split()))
n = 0
u = 0
flag = True
while flag:
    for i in range(N):
        u = A[i] // 2
        if A[i] % 2 == 1:
            flag = False
        else:
            A[i] = u
            continue
    if flag:
        n += 1
print(n)
