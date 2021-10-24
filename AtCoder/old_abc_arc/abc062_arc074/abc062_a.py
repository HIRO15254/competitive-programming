k = [1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]
N, M = map(int, input().split())
if k[N - 1] == k[M - 1]:
    print("Yes")
else:
    print("No")
