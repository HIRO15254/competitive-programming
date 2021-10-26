k = 0
N = int(input())
S = list(input())
for i in range(N):
    if k == 0 and S[i] == "I":
        k += 1
    if k == 1 and S[i] == "O":
        k += 1
    if k == 2 and S[i] == "I":
        k += 1
if k == 3:
    print("Yes")
else:
    print("No")
