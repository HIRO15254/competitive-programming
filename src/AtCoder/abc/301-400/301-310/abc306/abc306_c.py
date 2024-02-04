N = int(input())
c = [0] * N
A = list(map(int, input().split()))
ans = []
for i in range(N * 3):
    c[A[i] - 1] += 1
    if c[A[i] - 1] == 2:
        ans.append(A[i])
print(" ".join(map(str, ans)))
