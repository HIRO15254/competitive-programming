N, M, Q = map(int, input().rstrip().split(" "))
Point = [N] * M
Solve = [[False for _ in range(M)] for _ in range(N)]
ans = 0
for i in range(Q):
    s = list(map(int, input().rstrip().split(" ")))
    if s[0] == 1:
        ans = 0
        for i in range(M):
            if Solve[s[1] - 1][i]:
                ans += Point[i]
        print(ans)
    else:
        Point[s[2] - 1] -= 1
        Solve[s[1] - 1][s[2] - 1] = True
