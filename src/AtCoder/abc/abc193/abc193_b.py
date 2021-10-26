N = int(input())
ans = 10 ** 18
for i in range(N):
    A, P, X = map(int, input().split(" "))
    if X > A:
        ans = min(P, ans)
if ans == 10 ** 18:
    print(-1)
else:
    print(ans)
