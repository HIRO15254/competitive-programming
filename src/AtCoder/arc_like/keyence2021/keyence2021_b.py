N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
L = [0] * (N + 2)
for i in A:
    L[i] += 1
L[0] = min(L[0], K)
for i in range(1, N):
    L[i] = min(L[i - 1], L[i], K)
print(sum(L))
