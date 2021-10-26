N = int(input())
A = list(map(int, input().split(" ")))
ans = [1] * N
for i in range(N):
    now = A[i]
    while now != i + 1:
        now = A[now - 1]
        ans[i] += 1
print(" ".join(map(str, ans)))
