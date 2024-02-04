k = set()
N = int(input())
for _ in range(N):
    k.add(input())
l = list(k)
l2 = []
for S in l:
    if S[0] == "!":
        l2.append(S[1:])
    else:
        l2.append(S)
l2.sort()
for i in range(len(l2) - 1):
    if l2[i] == l2[i + 1]:
        print(l2[i])
        break
else:
    print("satisfiable")
