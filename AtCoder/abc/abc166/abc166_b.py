N, K = map(int, input().split(" "))
ans = N
snuke = [False] * (N + 1)
for i in range(K):
    d = int(input())
    A = list(map(int, input().rstrip().split(" ")))
    for i2 in range(d):
        if snuke[A[i2]] is False:
            snuke[A[i2]] = True
            ans -= 1
print(ans)
