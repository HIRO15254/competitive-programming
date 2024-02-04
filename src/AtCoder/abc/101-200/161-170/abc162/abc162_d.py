N = int(input())
R = []
G = []
B = []
s = input()
ans = 0
for i in range(N):
    if s[i] == "R":
        R.append(i)
    elif s[i] == "G":
        G.append(i)
    else:
        B.append(i)
sB = set(B)
ans = len(R) * len(G) * len(B)
for r in R:
    for g in G:
        i = min(r, g)
        j = max(r, g)
        sa = j - i
        if i - sa in sB:
            ans -= 1
        if j + sa in sB:
            ans -= 1
        if (i + j) / 2 in sB:
            ans -= 1
print(ans)
