M, N = input().rstrip().split(" ")
N2 = 0
N2 += int(N[0]) * 100
N2 += int(N[2]) * 10
N2 += int(N[3])

M = int(M) * 100

print((N2 * M) // 10000)
