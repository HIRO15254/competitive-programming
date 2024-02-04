N, M = map(int, input().rstrip().split(" "))
k = list(map(int, input().rstrip().split(" ")))
for i in range(M):
    N -= k[i]
if N >= 0:
    print(N)
else:
    print(-1)
