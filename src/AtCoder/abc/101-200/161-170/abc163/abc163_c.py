N = int(input())
k = list(map(int, input().rstrip().split(" ")))
p = [0 for _ in range(N)]
for i in range(N - 1):
    p[k[i] - 1] += 1
for i in range(N):
    print(p[i])
