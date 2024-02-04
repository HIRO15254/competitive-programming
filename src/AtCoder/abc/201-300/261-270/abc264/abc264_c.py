import itertools
H1, W1 = map(int, input().split())
A = []
for i in range(H1):
    A.append(list(map(int, input().split())))
H2, W2 = map(int, input().split())
B = []
for i in range(H2):
    B.append(list(map(int, input().split())))


def solve():
    for i in itertools.combinations(range(H1), H2):
        for j in itertools.combinations(range(W1), W2):
            end = False
            for i2 in range(H2):
                for j2 in range(W2):
                    if A[i[i2]][j[j2]] != B[i2][j2]:
                        end = True
                    if end:
                        break
                if end:
                    break
            else:
                return True
    return False


if solve():
    print("Yes")
else:
    print("No")
