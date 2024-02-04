N = int(input())
A = list(map(int, input().split()))
li = [[0, 0, 0] for _ in range(N + 1)]
ans = 0
p = 0
for i in range(N):
    if li[A[i]][0] == 0:
        li[A[i]] = [1, i, 0]
    else:
        p = (i - li[A[i]][1] - 1) * li[A[i]][0] + li[A[i]][2]
        ans += p
        li[A[i]] = [li[A[i]][0] + 1, i, p]
print(ans)
