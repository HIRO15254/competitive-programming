N, K, P = map(int, input().split())

ans = [10 ** 18] * ((P + 1) ** K)
ans[0] = 0


def add_param(x, y):
    x2 = []
    for i in range(K):
        x2.append(x // (P + 1) ** i % (P + 1))
    for i in range(K):
        x2[i] = min(x2[i] + y[i], P)
    ret = 0
    for i in range(K):
        ret += x2[i] * (P + 1) ** i
    return ret


for i in range(N):
    inp = list(map(int, input().split()))
    C = inp[0]
    A = inp[1:]
    for j in range((P + 1) ** K - 1, -1, -1):
        ans[add_param(j, A)] = min(ans[add_param(j, A)], ans[j] + C)
if ans[(P + 1) ** K - 1] == 10 ** 18:
    print(-1)
else:
    print(ans[(P + 1) ** K - 1])
