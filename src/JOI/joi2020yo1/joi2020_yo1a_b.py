_ = input()
S = list(input())
b = ['a', 'i', 'u', 'e', 'o']
ans = 0
for i in S:
    if i in b:
        ans += 1
print(ans)
