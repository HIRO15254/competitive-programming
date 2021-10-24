N = int(input())
p = list(map(int, input().rstrip().split(" ")))
ans = 0
swap = 0
for i in range(N):
    if p[i] == i + 1:
        if i != N - 1:
            swap = p[i]
            p[i] = p[i + 1]
            p[i + 1] = swap
            ans += 1
        else:
            swap = p[i]
            p[i] = p[i - 1]
            p[i - 1] = swap
            ans += 1
print(ans)
