ALP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = list(input())
ans = []
for i in S:
    ans.append(ALP[ALP.index(i) - 3])
print("".join(ans))
