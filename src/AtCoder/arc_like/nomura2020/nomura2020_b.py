T = list(input())
for i in range(len(T)):
    if T[i] == "?":
        T[i] = "D"
ans = "".join(T)
print(ans)
