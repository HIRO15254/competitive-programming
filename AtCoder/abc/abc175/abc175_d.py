N, K = map(int, input().rstrip().split(" "))
P = list(map(int, input().rstrip().split(" ")))
C = list(map(int, input().rstrip().split(" ")))

ans = -(10 ** 15)
for i in range(N):
    kans = 0
    score = [0]
    nex = P[i] - 1
    while True:
        score.append(score[-1] + C[nex])
        nex = P[nex] - 1
        if nex == P[i] - 1:
            break

    if score[-1] > 0:
        if score[1:(K % (len(score) - 1)) + 1] != []:
            kans = score[-1] * (K // (len(score) - 1)) + \
                max(score[1:(K % (len(score) - 1)) + 1])
        else:
            kans = score[-1] * ((K // (len(score) - 1)) - 1) + max(score)
    else:
        if score[1:min(len(score) - 1, K) + 1] != []:
            kans = max(score[1:min(len(score) - 1, K) + 1])
        else:
            kans = -(10 ** 15)
    ans = max(ans, kans)
print(ans)
