N = int(input())
k = []
ans = N
for i in range(N):
    k.append(input())
k.sort()
for i in range(N - 1):
    if k[i] == k[i + 1]:
        ans -= 1
print(ans)
