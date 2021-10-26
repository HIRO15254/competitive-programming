S = list(input())
s = 0
g = len(S) - 1
while S[s] != "A":
    s += 1
while S[g] != "Z":
    g -= 1
print(g - s + 1)
