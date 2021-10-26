N = int(input())
S = list(input())
for i in range(N - 2):
    if S[i:i + 3] == ['j', 'o', 'i']:
        S[i] = S[i].upper()
        S[i + 1] = S[i + 1].upper()
        S[i + 2] = S[i + 2].upper()
print("".join(S))
