arp = list(" abcdefghijklmnopqrstuvwxyz")
ans = []
N = int(input())
while N != 0:
    K = N % 26
    if K == 0:
        K = 26
    ans.append(arp[K])
    N -= K
    N = N // 26
ans.reverse()
print("".join(ans))
