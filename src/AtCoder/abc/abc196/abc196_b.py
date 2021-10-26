S = input()
ans = ""
for i in S:
    if i != ".":
        ans += i
    else:
        break
print(ans)
