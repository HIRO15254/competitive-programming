S = [[] for _ in range(16)]
S[0] = [1]
for i in range(15):
    S[i + 1] = S[i] + [i + 2] + S[i]
print(" ".join(list(map(str, S[int(input()) - 1]))))
