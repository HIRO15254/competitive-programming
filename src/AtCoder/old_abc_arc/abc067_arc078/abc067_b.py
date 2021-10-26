N, K = map(int, input().rstrip().split(" "))
I = list(map(int, input().rstrip().split(" ")))
I.sort(reverse=True)
ans = 0
for i in range(K):
    ans += I[i]
print(ans)
