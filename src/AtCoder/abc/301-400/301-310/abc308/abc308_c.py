from functools import cmp_to_key


def my_cmp(a, b):
    if a[1] * b[0] > a[0] * b[1]:
        return 1
    elif a[1] * b[0] < a[0] * b[1]:
        return -1
    else:
        if a[2] > b[2]:
            return 1
        elif a[2] < b[2]:
            return -1
    return 0


N = int(input())
h = []
for i in range(N):
    A, B = map(int, input().split())
    h.append((A, B, i + 1))
h.sort(key=cmp_to_key(my_cmp))
for i in range(N - 1):
    print(h[i][2], end=" ")
print(h[N - 1][2])
