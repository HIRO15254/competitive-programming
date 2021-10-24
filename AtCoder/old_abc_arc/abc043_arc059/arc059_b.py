s = list(input())
ans = [-1, -1]
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        ans = [i + 1, i + 2]
for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
        ans = [i + 1, i + 3]
print(" ".join(map(str, ans)))
