N, X = map(int, input().split(" "))
S = list(input())
ans = X
for i in S:
    if i == "o":
        ans += 1
    else:
        ans = max(ans - 1, 0)
print(ans)
