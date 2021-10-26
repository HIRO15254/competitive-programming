N, M = map(int, input().rstrip().split(" "))
K = [[]] * M
sw = [False] * N
count = 0
check = True
ans = 0

for i in range(M):
    K[i] = list(map(int, input().rstrip().split(" ")))
P = list(map(int, input().rstrip().split(" ")))


for i in range(2 ** N):
    check = True
    for i2 in range(N):
        sw[i2] = (i >> i2) & 1
    for i2 in range(M):
        counter = 0
        for i3 in range(K[i2][0]):
            if sw[K[i2][i3 + 1] - 1]:
                counter += 1
        if counter % 2 != P[i2]:
            check = False
            break
    if check:
        ans += 1
print(ans)
