N = int(input())
A = list(map(int, input().split(" ")))
ans = 0
c = 0
for i in range(N):
    if A[i] == 1:
        c += 1
        ans = max(c, ans)
    else:
        c = 0
print(ans + 1)
