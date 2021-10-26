O = list(input())
E = list(input())
ans = []
for i in range(len(E)):
    ans.append(O[i])
    ans.append(E[i])
if len(O) != len(E):
    ans.append(O[-1])
print("".join(ans))
