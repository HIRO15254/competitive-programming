X, Y, A, B, C = map(int, input().rstrip().split(" "))
RA = list(map(int, input().rstrip().split(" ")))
GA = list(map(int, input().rstrip().split(" ")))
WA = list(map(int, input().rstrip().split(" ")))
RA.sort()
RA.reverse()
GA.sort()
GA.reverse()
WA.sort()
WA.reverse()
eatRA = X
eatGA = Y
eatWA = 0
ans = 0
while RA[eatRA - 1] < WA[eatWA] or GA[eatGA - 1] < WA[eatWA]:
    n = 1
    while RA[eatRA - n] == GA[eatGA - n] and n != min(eatRA, eatGA):
        n += 1
    if RA[eatRA - n] > GA[eatGA - n]:
        eatGA -= 1
    else:
        eatRA -= 1
    eatWA += 1
    if eatWA == C or eatRA == 0 or eatGA == 0:
        break
if eatRA == 0 and eatGA != 0 and eatWA != C:
    while GA[eatGA - 1] < WA[eatWA]:
        eatGA -= 1
        eatWA += 1
        if eatWA == C or eatGA == 0:
            break
elif eatRA != 0 and eatGA == 0 and eatWA != C:
    while RA[eatRA - 1] < WA[eatWA]:
        eatRA -= 1
        eatWA += 1
        if eatWA == C or eatRA == 0:
            break
for i in range(eatRA):
    ans += RA[i]
for i in range(eatGA):
    ans += GA[i]
for i in range(eatWA):
    ans += WA[i]
print(ans)
