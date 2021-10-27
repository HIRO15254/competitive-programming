N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
amax = [A[0]]
bmax = 0
for i in range(1, N):
    amax.append(max(amax[-1], A[i]))
for i in range(N):
    bmax = max(bmax, B[i] * amax[i])
    print(bmax)
