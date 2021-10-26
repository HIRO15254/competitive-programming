S = input()
j = 0
o = 0
i = 0
ans = 0

for q in range(len(S)):
    if S[q] == "J":
        if q >= 1 and S[q - 1] != "J":
            j, o, i = 0, 0, 0
        j += 1
    elif S[q] == "O":
        if q >= 1 and S[q - 1] == "I":
            j, o, i = 0, 0, 0
        o += 1
    elif S[q] == "I":
        i += 1
        if j >= o and o == i:
            ans = max(ans, i)
print(ans)
