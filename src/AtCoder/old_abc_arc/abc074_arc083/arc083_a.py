A, B, C, D, E, F = map(int, input().split(" "))

# 30までの水の量を調べる

W = set()
W.add(A)
for i in range(30):
    if i in W:
        if i + A <= 30:
            W.add(i + A)
        if i + B <= 30:
            W.add(i + B)
S = set()
S.add(0)
for i in range(3000):
    if i in S:
        if i + C <= 3000:
            S.add(i + C)
        if i + D <= 3000:
            S.add(i + D)

ans_s = 0
ans_w = A
for w in W:
    for s in S:
        if w * 100 + s <= F:
            if s * ans_w > ans_s * w and E * w >= s:
                ans_s = s
                ans_w = w
print(ans_s + ans_w * 100, ans_s)
