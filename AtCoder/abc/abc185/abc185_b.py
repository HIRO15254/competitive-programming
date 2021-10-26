N, M, T = map(int, input().split(" "))
now = 0
N_now = N
for i in range(M):
    A, B = map(int, input().split(" "))
    N_now -= (A - now)
    if N_now <= 0:
        print("No")
        break
    N_now = min(N, N_now + (B - A))
    now = B
else:
    if N_now - (T - now) > 0:
        print("Yes")
    else:
        print("No")
