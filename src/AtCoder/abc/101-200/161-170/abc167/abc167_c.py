N, M, X = map(int, input().split(" "))
A = []
lis = []
rikai = [[0 for _ in range(M)]for _ in range(2 ** N)]
flag = True
kane = 0
ans = 10 ** 10
for i in range(N):
    A.append(list(map(int, input().split(" "))))

for i in range(2 ** N):
    lis.clear()
    kane = 0
    flag = True
    for i2 in range(N):
        if ((i >> i2) & 1):
            lis.append(i2)
    for i2 in lis:
        kane += A[i2][0]
        for i3 in range(M):
            rikai[i][i3] += A[i2][i3 + 1]
    for i2 in rikai[i]:
        if i2 < X:
            flag = False
    if flag:
        if ans > kane:
            ans = kane

if ans != 10 ** 10:
    print(ans)
else:
    print(-1)
