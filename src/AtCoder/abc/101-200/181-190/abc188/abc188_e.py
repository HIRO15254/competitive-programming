N, M = map(int, input().split(" "))
ya = [10 ** 18 for _ in range(N)]
A = list(map(int, input().split(" ")))
edge = []
for i in range(M):
    edge.append(list(map(int, input().split(" "))))
edge.sort()
for i in edge:
    ya[i[1] - 1] = min(ya[i[1] - 1], A[i[0] - 1], ya[i[0] - 1])
ans = -1 * 10 ** 19
for i in range(N):
    ans = max(ans, A[i] - ya[i])
print(ans)
