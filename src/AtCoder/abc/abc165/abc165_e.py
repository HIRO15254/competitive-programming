N, M = map(int, input().rstrip().split(" "))
ans = []
K = (N - 1) // 2
if K % 2 == 0:
    for i in range(K // 2):
        ans.append([K // 2 - i, K // 2 + i + 1])
    for i in range(K // 2):
        ans.append([N - K // 2 - 1 - i, N - K // 2 + i + 1])
else:
    for i in range(K // 2 + 1):
        ans.append([K // 2 + 1 - i, K // 2 + i + 2])
    for i in range(K // 2):
        ans.append([N - K // 2 - 1 - i, N - K // 2 + i + 1])
for i in range(M):
    print(str(ans[i][0]) + " " + str(ans[i][1]))
