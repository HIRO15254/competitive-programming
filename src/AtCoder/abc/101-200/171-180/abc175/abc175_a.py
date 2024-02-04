S = list(input())
stre = 0
ans = 0
for i in S:
    if i == "R":
        stre += 1
        if stre > ans:
            ans = stre
    else:
        stre = 0
print(ans)
