N, S = input().split(" ")
N = int(N)
S = list(S)
AGCT = [[0, 0, 0, 0] for i in range(N + 1)]
for i in range(len(S)):
    AGCT[i + 1][0] = AGCT[i][0]
    AGCT[i + 1][1] = AGCT[i][1]
    AGCT[i + 1][2] = AGCT[i][2]
    AGCT[i + 1][3] = AGCT[i][3]
    if S[i] == "A":
        AGCT[i + 1][0] += 1
    if S[i] == "G":
        AGCT[i + 1][1] += 1
    if S[i] == "C":
        AGCT[i + 1][2] += 1
    if S[i] == "T":
        AGCT[i + 1][3] += 1
ans = 0
for i in range(2, len(S) + 1, 2):
    for j in range(0, len(S) - i + 1):
        if AGCT[j + i][0] - AGCT[j][0] == AGCT[j + i][3] - AGCT[j][3] and AGCT[j + i][1] - AGCT[j][1] == AGCT[j + i][2] - AGCT[j][2]:
            ans += 1
print(ans)
