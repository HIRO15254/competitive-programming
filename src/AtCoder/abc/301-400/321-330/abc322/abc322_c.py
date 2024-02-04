N, M = map(int, input().split())
A = list(map(int, input().split()))
now = 0
for i in range(1, N + 1):
    if A[now] == i:
        print(0)
        now += 1
    else:
        print(A[now] - i)
