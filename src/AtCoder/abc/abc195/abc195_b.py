A, B, W = map(int, input().split(" "))
W *= 1000
mi = 0
ma = 0
now = 0
ans_mi = 10 ** 18
ans_ma = 0
while mi <= W:
    mi += A
    ma += B
    now += 1
    if (mi <= W and W <= ma):
        ans_mi = min(now, ans_mi)
        ans_ma = max(now, ans_ma)
if ans_ma == 0:
    print("UNSATISFIABLE")
else:
    print(ans_mi, ans_ma)
