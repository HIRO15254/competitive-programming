N, M, Q = map(int, input().rstrip().split(" "))
graph = [[]for _ in range(N + 1)]
for i in range(M):
    n = list(map(int, input().rstrip().split(" ")))
    graph[n[0]].append(n[1])
    graph[n[1]].append(n[0])
col = list(map(int, input().rstrip().split(" ")))
col.insert(0, 0)
for _ in range(Q):
    s = list(map(int, input().rstrip().split(" ")))
    if s[0] == 1:
        print(col[s[1]])
        for i in graph[s[1]]:
            col[i] = col[s[1]]
    else:
        print(col[s[1]])
        col[s[1]] = s[2]
