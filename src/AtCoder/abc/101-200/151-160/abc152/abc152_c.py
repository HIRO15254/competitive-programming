N = int(input())
a = input().rstrip().split()
P = [0] * N
for i in range(N):
    P[i] = int(a[i])
minP = P[0]
ans = 1
for i in range(N - 1):
    if minP >= P[i + 1]:
        ans += 1
        minP = P[i + 1]
print(ans)
