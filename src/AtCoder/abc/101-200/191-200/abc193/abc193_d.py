def point(a, b, c, d, e):
    cards = [a, b, c, d, e]
    p = 0
    for i in range(10):
        p += i * (10 ** cards.count(str(i)))
    return p


K = int(input())
S = list(input())
T = list(input())
left = [K] * 10

aa = (K * 9 - 8) * (K * 9 - 9)
ww = 0

for i in range(10):
    left[i] -= S.count(str(i)) + T.count(str(i))
for i in range(1, 10):
    if left[i] != 0:
        Sp = point(S[0], S[1], S[2], S[3], str(i))
        for j in range(1, 10):
            Tp = point(T[0], T[1], T[2], T[3], str(j))
            if Sp > Tp:
                if i == j:
                    ww += left[i] * (left[j] - 1)
                else:
                    ww += left[i] * left[j]
print(ww / aa)
