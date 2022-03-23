N = int(input())
A1 = list(map(int, input().split(" ")))
A2 = list(map(int, input().split(" ")))
now = A1[0] + sum(A2)
ans = now
for i in range(N - 1):
    now += A1[i + 1] - A2[i]
    ans = max(ans, now)
print(ans)
