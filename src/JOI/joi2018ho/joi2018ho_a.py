N, K = map(int, input().split(" "))
p = []
q = int(input())
for i in range(N - 1):
    r = int(input())
    p.append(r - q - 1)
    q = r
p.sort()
ans = N
for i in range(N - K):
    ans += p[i]
print(ans)
