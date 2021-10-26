S = input()
hug = 0
for i in range(int(len(S) / 2)):
    if not S[i] == S[(i + 1) * -1]:
        hug += 1
print(hug)
