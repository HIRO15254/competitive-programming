N = int(input())
ans = 0
A = list(map(int, input().rstrip().split(" ")))
for i in range(0, N, 2):
    if A[i] % 2 == 1:
        ans += 1
print(ans)
