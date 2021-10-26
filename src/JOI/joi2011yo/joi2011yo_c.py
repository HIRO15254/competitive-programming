N = int(input())
K = int(input())
for i in range(K):
    x, y = map(int, input().split(" "))
    print(min(min(x - 1, N - x), min(y - 1, N - y)) % 3 + 1)
