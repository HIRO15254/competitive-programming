def kap(a):
    Sa = list(str(a))
    Sa.sort()
    Sa.reverse()
    ansa = int("".join(Sa))
    Sb = list(str(a))
    Sb.sort()
    ansb = int("".join(Sb))
    return int(ansa) - int(ansb)


N, K = map(int, input().split(" "))
ans = N
for i in range(K):
    ans = kap(ans)
print(ans)
