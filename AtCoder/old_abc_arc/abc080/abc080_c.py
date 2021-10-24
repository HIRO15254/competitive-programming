N = int(input())
F = []
P = []
ans = -1 * (10 ** 18)
for i in range(N):
    F.append(list(map(int, input().split(" "))))
for i in range(N):
    P.append(list(map(int, input().split(" "))))
for i in range(1, 2**10):
    c = 0
    for j in range(N):
        counter = 0
        for k in range(10):
            if i >> k & F[j][k]:
                counter += 1
        c += P[j][counter]
    ans = max(c, ans)
print(ans)
