N, X = map(int, input().split())


def make_ans(m, X, from_min):
    ma = m
    if ma == X:
        ma -= 1
    mi = 1
    if mi == X:
        mi += 1
    ret = []
    if from_min:
        while len(ret) != (m - 1):
            if len(ret) % 2 != 0:
                ret.append(ma)
                ma -= 1
                if ma == X:
                    ma -= 1
            else:
                ret.append(mi)
                mi += 1
                if mi == X:
                    mi += 1
            if ma == mi:
                ret.append(ma)
                break
    else:
        while len(ret) != (m - 1):
            if len(ret) % 2 == 0:
                ret.append(ma)
                ma -= 1
                if ma == X:
                    ma -= 1
            else:
                ret.append(mi)
                mi += 1
                if mi == X:
                    mi += 1
    ret.reverse()
    return ret


print(" ".join(map(str, [X] + make_ans(N, X, N % 2 == 0 and X == (N // 2 + 1)))))