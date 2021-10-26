N, K = map(int, input().rstrip().split(" "))
print(min(N % K, abs(N % K - K)))
