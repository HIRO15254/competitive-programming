N = int(input())
A = list(map(int, input().split(" ")))
k = []
p = 1
for i in range(N - 1):
    if A[i] == A[i + 1]:
        k.append(p)
        p = 1
    else:
        p += 1
k.append(p)

if len(k) <= 3:
    ans = sum(k)
else:
    q = k[0] + k[1] + k[2]
    ans = q
    for i in range(len(k) - 3):
        q -= k[i]
        q += k[i + 3]
        ans = max(ans, q)
print(ans)
