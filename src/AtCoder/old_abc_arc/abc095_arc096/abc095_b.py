N, X = map(int, input().split())
M = []
for _ in range(N):
    M.append(int(input()))
M.sort()
print(N + ((X - sum(M)) // M[0]))