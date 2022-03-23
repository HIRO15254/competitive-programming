T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = 0
    B_old = 0
    B_new = 0
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if i == 0:
            ans = x
        B_new = B_old + x * y
        if B_new < 0 and B_old > 0:
            n = B_old // abs(x)
            B_new_2 = B_old + x * n
            ans_c = A + ((B_old + B_new_2 + x) * n) // 2
            if ans_c > ans:
                ans = ans_c
        A += (B_old + B_new + x) * y // 2
        if ans < A:
            ans = A
        B_old = B_new
    print(ans)