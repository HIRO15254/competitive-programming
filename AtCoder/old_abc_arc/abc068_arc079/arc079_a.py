N, M = map(int, input().rstrip().split(" "))
G = [[] for i in range(N + 1)]
ans = False
for i in range(M):
    a, b = map(int, input().rstrip().split(" "))
    G[a].append(b)
    G[b].append(a)
for i in G[1]:
    if (N in G[i]):
        ans = True
if ans:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
