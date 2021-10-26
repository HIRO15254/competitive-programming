N = int(input())
K = [[], [], []]
ans = [0] * N
for i in range(N):
    A = list(map(int, input().split(" ")))
    for i in range(3):
        K[i].append(A[i])
for i in range(3):
    for j in range(N):
        if K[i].count(K[i][j]) == 1:
            ans[j] += K[i][j]
for i in range(N):
    print(ans[i])
