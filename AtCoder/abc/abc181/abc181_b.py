N = int(input())
ans = 0
for i in range(N):
    a, b = map(int, input().split(" "))
    ans += (a + b) * (b - a + 1)
print(int(ans / 2))
