N, K = map(int, input().rstrip().split(" "))
A = [list(map(int, input().rstrip().split(" ")))]
imos = [0 for i in range(N + 1)]
P = 0
flag = True
counter = 0
while flag:
    A.append([0 for i in range(N)])
    P = 0
    for i in range(N + 1):
        imos[i] = 0
    for i in range(N):
        imos[max(0, i - A[counter][i])] += 1
        imos[min(N, i + A[counter][i] + 1)] -= 1
    if imos[0] == N and imos[N] == -1 * N:
        flag = False
    for i in range(N):
        P += imos[i]
        A[counter + 1][i] = P
    counter += 1
    if counter == K:
        break
print(" ".join(map(str, A[-1])))
