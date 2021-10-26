N = int(input())
M = int(input())
q = [[] for _ in range(N + 1)]
ans = set()
ans.add(1)
for _ in range(M):
    a, b = map(int, input().split(" "))
    q[a].append(b)
    q[b].append(a)
for i in q[1]:
    ans.add(i)
    for j in q[i]:
        ans.add(j)

print(len(ans) - 1)
