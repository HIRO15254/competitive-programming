N = int(input())
P = list(map(int, input().split()))

ans = []

def d_ins(i, j):
    ans.append((i, j))
    d1 = P.pop(i)
    d2 = P.pop(i)
    P.insert(j, d2)
    P.insert(j, d1)


for i in range(N - 1):
    if P[i] != i + 1:
        ind = P.index(i + 1)
        if ind == N - 1:
            if i == N - 2:
                continue
            d_ins(ind - 1, i)
            d_ins(i + 1, i)
        else:
            d_ins(ind, i)
if P != list(range(1, N + 1)):
    print("No")
else:
    print("Yes")
    print(len(ans))
    for i in ans:
        print(i[0] + 1, i[1])
