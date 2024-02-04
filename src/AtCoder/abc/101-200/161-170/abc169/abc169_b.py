N = int(input())
A = list(map(int, input().rstrip().split(" ")))
flag = True
ans = 1
for i in range(N):
    if A[i] == 0:
        ans = 0
for i in range(N):
    ans *= A[i]
    if ans > 10 ** 18:
        flag = False
        break
if flag:
    print(ans)
else:
    print(-1)
