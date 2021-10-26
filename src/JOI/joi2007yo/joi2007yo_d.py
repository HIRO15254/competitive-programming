import copy
n = int(input())
m = int(input())
c = [i for i in range(1, 2 * n + 1)]
q = []
for _ in range(m):
    k = int(input())
    if k == 0:
        for i in range(n):
            q.append(c[i])
            q.append(c[n + i])
        c = q
        q = []
    else:
        for i in range(n * 2 - k):
            q.append(c[k + i])
        for i in range(k):
            q.append(c[i])
        c = q
        q = []
for i in range(2 * n):
    print(c[i])
