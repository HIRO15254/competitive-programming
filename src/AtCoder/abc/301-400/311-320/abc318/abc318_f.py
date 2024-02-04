from copy import deepcopy

N = int(input())
X = list(map(int, input().split()))
L = list(map(int, input().split()))
X.sort()
L.sort(reverse=True)


def imos_slesh(imos, slesh):
    ret = []
    imos.sort()
    now = 0
    for i in imos:
        if i[1] == -1:
            now += 1
            if now == slesh:
                ret.append([i[0], -1])
        else:
            if now == slesh:
                ret.append([i[0], 1])
            now -= 1
    return ret


def imos_to_ans(imos):
    ret = 0
    for i in range(len(imos) // 2):
        ret += imos[i * 2 + 1][0] - imos[i * 2][0] + 1
    return ret


# [n番目に長い腕][一番右をつかんだ回数]
dp = [[[] for _ in range(i + 1)] for i in range(N + 1)]
dp[0][0].append([-10 ** 18 - 10, -1])
dp[0][0].append([10 ** 18 + 10, 1])
# imosをして1になるところは、今のところ問題なし
for i in range(N):
    for j in range(i + 1):
        left_dp = deepcopy(dp[i][j])
        right_dp = deepcopy(dp[i][j])
        left_dp.append([X[i - j] - L[i], -1])
        left_dp.append([X[i - j] + L[i], 1])
        dp[i + 1][j] += imos_slesh(left_dp, 2)
        right_dp.append([X[(N - 1 - j)] - L[i], -1])
        right_dp.append([X[(N - 1 - j)] + L[i], 1])
        dp[i + 1][j + 1] += imos_slesh(right_dp, 2)
    # imosをして、2以上になるところを次に持っていく
    for j in range(i + 1):
        dp[i + 1][j] = imos_slesh(dp[i + 1][j], 1)
last_imos = []
for i in range(N + 1):
    last_imos += dp[N][i]
last_imos = imos_slesh(last_imos, 1)
print(imos_to_ans(last_imos))
