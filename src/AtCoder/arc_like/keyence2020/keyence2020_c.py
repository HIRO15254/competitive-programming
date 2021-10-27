N, K, S = map(int, input().rstrip().split(" "))
ans = []
if S != 10 ** 9:
    for i in range(K):
        ans.append(S)
    for i in range(N - K):
        ans.append(S + 1)
else:
    for i in range(K):
        ans.append(S)
    for i in range(N - K):
        ans.append(1)
print(" ".join(map(str, ans)))
