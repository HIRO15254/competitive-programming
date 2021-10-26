S = input()
ans = 0
for i in range(1, len(S) // 2):
    if str(S[0:i]) == str(S[i:i * 2]):
        ans = i * 2
print(ans)
