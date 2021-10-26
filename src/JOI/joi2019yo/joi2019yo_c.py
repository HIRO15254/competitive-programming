N = int(input())
S = input()
i = 0
ans = 0
while i < N - 1:
    if S[i:i + 2] == "OX" or S[i:i + 2] == "XO":
        ans += 1
        i += 1
    i += 1
print(ans)
