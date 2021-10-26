N = int(input())
Po = []
for i in range(N):
    Po.append(list(map(int, input().split(" "))))
ans = False
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and i != k and j != k:
                if (Po[i][0] - Po[j][0]) * (Po[i][1] - Po[k][1]) == (Po[i][1] - Po[j][1]) * (Po[i][0] - Po[k][0]):
                    ans = True
if ans:
    print("Yes")
else:
    print("No")
