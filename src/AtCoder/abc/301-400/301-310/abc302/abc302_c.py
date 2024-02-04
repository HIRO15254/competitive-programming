import itertools


def alm_eq(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c == 1


N, M = map(int, input().split())
S = [input() for _ in range(N)]

for i in itertools.permutations(S):
    for j in range(N - 1):
        if not alm_eq(i[j], i[j + 1]):
            break
    else:
        print("Yes")
        exit()
print("No")
