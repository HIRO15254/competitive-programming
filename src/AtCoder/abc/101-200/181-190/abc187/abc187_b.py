N = int(input())
p = []
for _ in range(N):
    x, y = map(int, input().split(" "))
    p.append([x, y])
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if abs(p[i][0] - p[j][0]) >= abs(p[i][1] - p[j][1]):
            ans += 1
print(ans)
