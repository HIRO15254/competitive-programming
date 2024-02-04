N, M = map(int, input().rstrip().split(" "))
ans = 0
n = [-1 for i in range(N)]
for i in range(M):
    s, c = map(int, input().rstrip().split(" "))
    s -= 1
    if n[s] == -1 or n[s] == c:
        n[s] = c
    else:
        ans = -1
if N != 1 and n[0] == 0:
    ans = -1

if ans == -1:
    print(-1)
elif N == 1 and M == 0:
    print(0)
else:
    for i in range(N):
        if n[i] == -1:
            if i == 0:
                ans += 10 ** (N - 1)
        else:
            ans += 10 ** (N - i - 1) * n[i]
    print(ans)
