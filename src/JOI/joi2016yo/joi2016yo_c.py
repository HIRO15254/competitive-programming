N, M = map(int, input().split(" "))
F = []
ans = 10 ** 9
for i in range(N):
    S = list(input())
    W = S.count("W")
    B = S.count("B")
    R = S.count("R")
    F.append([W, B, R])
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k_ans = 0
        for k in range(N):
            if k <= i:
                k_ans += M - F[k][0]
            elif k <= j:
                k_ans += M - F[k][1]
            else:
                k_ans += M - F[k][2]
        ans = min(ans, k_ans)
print(ans)
