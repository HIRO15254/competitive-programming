N, M = map(int, input().rstrip().split(" "))
ans = [False for _ in range(N + 1)]
balls = [1 for _ in range(N + 1)]
ans[1] = True
for i in range(M):
    q = list(map(int, input().rstrip().split(" ")))
    if ans[q[0]] is True:
        ans[q[1]] = True
    balls[q[0]] -= 1
    if balls[q[0]] == 0:
        ans[q[0]] = False
    balls[q[1]] += 1
ansi = 0
for i in range(N + 1):
    if ans[i]:
        ansi += 1
print(ansi)
