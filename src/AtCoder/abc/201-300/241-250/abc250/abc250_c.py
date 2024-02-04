from tkinter import Y


N, Q = map(int, input().split())
p_n = list(range(N))
n_p = list(range(N))
for _ in range(Q):
    x = int(input()) - 1
    p = n_p[x]
    y = p_n[p + 1 if p + 1 < N else p - 1]
    p_n[p + 1 if p + 1 < N else p - 1] = x
    p_n[p] = y
    n_p[x] = p + 1 if p + 1 < N else p - 1
    n_p[y] = p
print(" ".join(list(map(lambda x: str(x + 1), p_n))))
