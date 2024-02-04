S = list(input())
S.sort()
S.append("10")
for i in range(10):
    if int(S[i]) != i:
        print(i)
        break
