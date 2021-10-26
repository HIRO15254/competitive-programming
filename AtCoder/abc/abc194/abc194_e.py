N, M = map(int, input().split())
A = list(map(int, input().split()))
c = [[-1] for _ in range(N)]
for i in range(N):
    c[A[i]].append(i)
for i in range(N):
    c[i].append(N)
for i in range(N):
    end = False
    for j in range(len(c[i]) - 1):
        if c[i][j + 1] - c[i][j] > M:
            end = True
    if end:
        print(i)
        break
else:
    print(N)
