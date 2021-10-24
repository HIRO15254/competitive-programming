n = [0 for _ in range(26)]
S = list(input())
ans = "Yes"
for i in S:
    n[ord(i) - ord('a')] += 1
for i in n:
    if i % 2 != 0:
        ans = "No"
print(ans)
