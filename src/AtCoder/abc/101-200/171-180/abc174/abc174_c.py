K = int(input())
p = 7 % K
ans = 1
for i in range(K):
    if p == 0:
        print(ans)
        break
    p2 = (p * 10) % K
    p = 7 % K + p2
    p %= K
    ans += 1
if p != 0:
    print(-1)
