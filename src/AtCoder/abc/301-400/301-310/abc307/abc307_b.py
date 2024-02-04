def kaibun(S):
    for i in range(len(S) // 2):
        if S[i] != S[-i - 1]:
            return False
    return True


N = int(input())
S = []
for i in range(N):
    S.append(input())
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if kaibun(S[i] + S[j]):
            print("Yes")
            exit()
print("No")
