S = list(input())
s = []
q = 0
ans = 0
for i in S:
    s.append(int(i))
for i in range(2 ** len(s)):
    for i2 in range(len(s)):
        if i >> i2 & 1:
            ans += q
            q = s[i2]
        else:
            q *= 10
    ans += q
    q = 0
print(ans)
