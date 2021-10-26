N = int(input())
Alist = []
Blist = []
ans = 10 ** 18
for i in range(N):
    A, B = map(int, input().split())
    Alist.append(A)
    Blist.append(B)
for i in range(N):
    for j in range(N):
        if i == j:
            ans = min(Alist[i] + Blist[j], ans)
        else:
            ans = min(max(Alist[i], Blist[j]), ans)
print(ans)
