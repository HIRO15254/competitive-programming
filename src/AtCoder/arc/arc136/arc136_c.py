N = int(input())
A = list(map(int, input().split()))

ans = [0] * (10 ** 2)
for i in A:
    ans[i] += 1
for i in range(10 ** 1):
    for j in range(9):
        ans[i * 10 + j + 1] += ans[i * 10 + j]
print(ans)