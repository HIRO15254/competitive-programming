import itertools
N, K = map(int, input().split(" "))
ls = list(itertools.permutations(range(1, N)))
dist = []
for i in range(N):
    dist.append(list(map(int, input().split(" "))))
ans = 0
for i in ls:
    dis = dist[0][i[0]]
    for j in range(N - 2):
        dis += dist[i[j]][i[j + 1]]
    dis += dist[i[-1]][0]
    if dis == K:
        ans += 1
print(ans)
