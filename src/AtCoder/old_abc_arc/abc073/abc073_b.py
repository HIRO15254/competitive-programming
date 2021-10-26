N = int(input())
ans = 0
for _ in range(N):
    l, r = map(int, input().rstrip().split(" "))
    ans += r - l + 1
print(ans)
