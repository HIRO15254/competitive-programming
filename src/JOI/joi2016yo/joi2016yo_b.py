N, M = map(int, input().split(" "))
z = []
for i in range(N):
    z.append(int(input()))
for i in range(1, M + 1):
    for j in range(N - 1):
        if z[j] % i > z[j + 1] % i:
            z[j], z[j + 1] = z[j + 1], z[j]
for i in z:
    print(i)
