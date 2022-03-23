N = int(input())
X = list(map(int, input().split()))
X2 = sorted(X)
M_1 = X2[N // 2 - 1]
M_2 = X2[N // 2]
for i in range(N):
    if X[i] <= M_1:
        print(M_2)
    else:
        print(M_1)
