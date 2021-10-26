N = int(input())
ans = 0
for i in range(N):
    A, T = map(int, input().rstrip().split(" "))
    ans = max(ans, A + T)
    ans = max(ans, A * 2)
print(ans)
