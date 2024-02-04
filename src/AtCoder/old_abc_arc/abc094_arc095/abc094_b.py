N, M, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in A:
    if i < X:
        ans += 1
print(min(ans, M - ans))