N = list(input())
N.reverse()
ans = 18
for i in range(2 ** len(N)):
    p = 0
    k = 0
    for j in range(len(N)):
        if i & 1 << j:
            p += int(N[j])
        else:
            k += 1
    if p % 3 == 0:
        ans = min(ans, k)
if ans == len(N):
    ans = -1
print(ans)
