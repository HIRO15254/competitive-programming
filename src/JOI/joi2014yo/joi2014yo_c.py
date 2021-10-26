W, H, N = map(int, input().split(" "))
x, y = map(int, input().split(" "))
ans = 0
for i in range(N - 1):
    x2, y2 = map(int, input().split(" "))
    q = 0
    if ((x - x2) < 0) == ((y - y2) < 0):
        q = min(abs(x - x2), abs(y - y2))
    ans += abs(x - x2) + abs(y - y2) - q
    x, y = x2, y2
print(ans)
