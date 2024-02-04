N, K = map(int, input().split(" "))
P = []
P2 = []
for i in range(N):
    p = sum(list(map(int, input().split(" "))))
    P.append(p)
    P2.append(p)
P2.sort(reverse=True)
border = P2[K - 1]
for i in range(N):
    if P[i] + 300 >= border:
        print("Yes")
    else:
        print("No")
