A, B, K = map(int, input().split())
if B - A + 1 > K * 2:
    for i in range(A, A + K):
        print(i)
    for i in range(B - K, B):
        print(i + 1)
else:
    for i in range(A, B + 1):
        print(i)