Seiza = []
m = int(input())
for _ in range(m):
    x, y = map(int, input().split(" "))
    Seiza.append([x, y])
Seiza.sort()
Hoshi = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split(" "))
    Hoshi.append([x, y])
Hoshi.sort()

sa = []
step = 0
for i in range(n):
    sa = [Seiza[0][0] - Hoshi[i][0], Seiza[0][1] - Hoshi[i][1]]
    step = 1
    for k in range(i, n):
        if Seiza[step][0] == Hoshi[k][0] + sa[0] and Seiza[step][1] == Hoshi[k][1] + sa[1]:
            step += 1
            if step == m:
                print(-1 * sa[0], -1 * sa[1])
                break
