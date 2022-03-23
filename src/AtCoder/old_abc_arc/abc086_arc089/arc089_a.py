N = int(input())
Q = [[0, 0, 0]]
ans = True
for i in range(N):
    t, x, y = map(int, input().split(" "))
    Q.append([t - Q[-1][0], x - Q[-1][1], y - Q[-1][2]])
for i in Q:
    if abs(i[1]) + abs(i[2]) > i[0] or (i[1] + i[2]) % 2 != i[0] % 2:
        print("No")
        exit()
print("Yes")
