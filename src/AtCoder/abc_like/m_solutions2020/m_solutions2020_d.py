N = int(input())
A = list(map(int, input().rstrip().split(" ")))
uru = [0, 0]
uruold = [0, 1000]
kau = [0, 0]
kauold = [1000 // A[0], 1000 % A[0]]
for i in range(N):
    if uruold[0] * A[i] + uruold[1] < kauold[0] * A[i] + kauold[1]:
        uru[0] = 0
        uru[1] = kau[0] * A[i] + kau[1]
    else:
        uru = uruold
    if uruold[1] // A[i] + uruold[0] > kauold[1] // A[i] + kauold[0] or (uruold[1] // A[i] + uruold[0] == kauold[1] // A[i] + kauold[0] and uruold[1] % A[i] > kauold[1] % A[i]):
        kau[0] = uruold[1] // A[i] + uruold[0]
        kau[1] = uruold[1] % A[i]
    else:
        kau = kauold
    uruold = uru
    kauold = kau
print(max(uru[1] + uru[0] * A[N - 1], kau[1] + kau[0] * A[N - 1]))
