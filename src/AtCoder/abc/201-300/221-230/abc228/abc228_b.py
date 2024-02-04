N, X = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
know = [0] * N
now = X - 1
know[now] = 1
while know[A[now] - 1] != 1:
    know[A[now] - 1] = 1
    now = A[now] - 1
print(sum(know))
