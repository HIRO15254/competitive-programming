H, W, M = map(int, input().rstrip().split(" "))
B = set()
Hc = [0 for i in range(H)]
Wc = [0 for i in range(W)]
Hl = []
Wl = []
for i in range(M):
    h, w = map(int, input().rstrip().split(" "))
    Hc[h - 1] += 1
    Wc[w - 1] += 1
    B.add((h - 1) * W + w - 1)
Hm = max(Hc)
Wm = max(Wc)
ans = 0
for i in range(H):
    if Hc[i] == Hm:
        Hl.append(i)
for i in range(W):
    if Wc[i] == Wm:
        Wl.append(i)
if len(Hl) * len(Wl) > M:
    ans = Hm + Wm
else:
    for h in Hl:
        for w in Wl:
            if not h * W + w in B:
                ans = Hm + Wm
                break
    if ans == 0:
        ans = Hm + Wm - 1
print(ans)
