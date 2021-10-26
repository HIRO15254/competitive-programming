N, K = map(int, input().rstrip().split())
ans = [0 for _ in range(10 ** 5 + 1)]
for i in range(N):
    a, b = map(int, input().rstrip().split())
    ans[a] += b
counter = 0
c2 = 0
while counter < K:
    c2 += 1
    counter += ans[c2]
print(c2)
