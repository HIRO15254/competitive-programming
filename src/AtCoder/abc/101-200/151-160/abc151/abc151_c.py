N, M = map(int, input().rstrip().split(" "))
ans = [False for _ in range(N + 1)]
wa = [0 for _ in range(N + 1)]
ansi = 0
penai = 0
for i in range(M):
    k = input().rstrip().split(" ")
    if ans[int(k[0])] is False:
        if k[1] == "AC":
            ans[int(k[0])] = True
            penai += wa[int(k[0])]
            ansi += 1
        else:
            wa[int(k[0])] += 1
print(str(ansi) + " " + str(penai))
