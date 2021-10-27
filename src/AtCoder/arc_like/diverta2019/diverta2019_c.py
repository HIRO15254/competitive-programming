N = int(input())
ans = 0
f = False
xx = 0
xA = 0
Bx = 0
BA = 0
A = 0
B = 0
for i in range(N):
    S = input()
    for i in range(len(S) - 1):
        if S[i] == "A" and S[i + 1] == "B":
            ans += 1
    if S[0] == "B":
        if S[-1] == "A":
            BA += 1
        else:
            Bx += 1
    else:
        if S[-1] == "A":
            xA += 1
if xA != 0 and Bx != 0:
    ans += BA + 1
    xA -= 1
    Bx -= 1
elif xA != 0:
    ans += BA
    xA -= 1
elif Bx != 0:
    ans += BA
    Bx -= 1
else:
    if BA >= 2:
        ans += BA - 1
ans += min(Bx, xA)
print(ans)
