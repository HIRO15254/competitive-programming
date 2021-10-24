N, K = map(int, input().rstrip().split(" "))
print(K * (K - 1) ** (N - 1))
