s = list(input())
ans = []
for i in s:
    if i == 'B':
        if len(ans) != 0:
            ans.pop()
    else:
        ans.append(i)
print("".join(ans))
