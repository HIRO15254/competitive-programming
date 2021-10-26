import itertools


def match(c, S):
    for i in range(len(S) - len(c) + 1):
        for j in range(len(c)):
            if S[i + j] == c[j] or c[j] == '.':
                if j == len(c) - 1:
                    return True
            else:
                break
    return False


S = input()
alp = "abcdefghijklmnopqrstuvwxyz."
ans = 0
for j in range(3):
    for i in itertools.product(alp, repeat=(j + 1)):
        if match(i, S):
            ans += 1
print(ans)
