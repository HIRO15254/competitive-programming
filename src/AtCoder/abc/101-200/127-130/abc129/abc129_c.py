N, M = map(int, input().rstrip().split(" "))
ans = [0 for _ in range(N + 3)]
ans[0] = 1
m = []
mc = 0
for _ in range(M):
    m.append(int(input()))
m.append(0)
for i in range(1, N + 1):
    if m[mc] != i:
        ans[i] += ans[i - 1]
        ans[i] += ans[i - 2]
        ans[i] %= 1000000007
    else:
        mc += 1
print(ans[N])
