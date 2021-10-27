N = int(input())
A = list(map(int, input().rstrip().split(" ")))
yuyo = [0] * (N + 1)
nokori = [0] * (N + 2)
A.append(0)
nokori[N + 1] = 0
ans = 0
for i in range(N, -1, -1):
    nokori[i] = nokori[i + 1] + A[i + 1]
ans = 0
if A[0] != 0:
    if A[0] == 1 and N == 0:
        ans = 1
    else:
        ans = -1
else:
    yuyo[0] = 1
    for i in range(1, N + 1):
        yuyo[i] = min(yuyo[i - 1] * 2 - A[i], nokori[i])
        if yuyo[i] < 0:
            ans = -1
            break
if ans == -1:
    print(-1)
else:
    for i in range(N):
        ans += yuyo[i]
    ans += nokori[0]
    print(ans)
