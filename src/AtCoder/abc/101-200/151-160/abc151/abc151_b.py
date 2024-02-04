N, K, M = map(int, input().rstrip().split(" "))
k = list(map(int, input().rstrip().split(" ")))
point = 0
for i in k:
    point += i
if point >= N * M:
    print(0)
elif point + K < N * M:
    print(-1)
else:
    print(N * M - point)
