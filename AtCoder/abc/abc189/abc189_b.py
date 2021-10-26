N, X = map(int, input().split(" "))
alc = 0
for i in range(N):
    v, p = map(int, input().split(" "))
    alc += v * p
    if alc > X * 100:
        print(i + 1)
        break
else:
    print(-1)
