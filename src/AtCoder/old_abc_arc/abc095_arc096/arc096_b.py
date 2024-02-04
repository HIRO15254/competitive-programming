N, C = map(int, input().split())
sushi = []
for i in range(N):
    x, v = map(int, input().split())
    sushi.append([x, v])
sushi.sort()
for i in range(N):
    