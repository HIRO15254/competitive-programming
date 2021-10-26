N, M = map(int, input().split(" "))
H = list(map(int, input().rstrip().split(" ")))
ans = [True] * N
ansi = N
for i in range(M):
    K = list(map(int, input().rstrip().split(" ")))
    if (H[K[0] - 1] > H[K[1] - 1]):
        if ans[K[1] - 1] is True:
            ans[K[1] - 1] = False
            ansi -= 1
    elif (H[K[0] - 1] < H[K[1] - 1]):
        if ans[K[0] - 1] is True:
            ans[K[0] - 1] = False
            ansi -= 1
    else:
        if ans[K[1] - 1] is True:
            ans[K[1] - 1] = False
            ansi -= 1
        if ans[K[0] - 1] is True:
            ans[K[0] - 1] = False
            ansi -= 1
print(ansi)
