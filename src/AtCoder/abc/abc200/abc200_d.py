N = int(input())
A = list(map(int, input().split(" ")))
k = [[] for _ in range(200)]
for i in range(1, 2 ** min(16, N)):
    p = 0
    for j in range(min(16, N)):
        if (i >> j) & 1:
            p += A[j]
            p %= 200
    k[p].append(i)
for i in k:
    if len(i) >= 2:
        print("Yes")
        q = [0]
        for j in range(min(16, N)):
            if (i[0] >> j) & 1:
                q[0] += 1
                q.append(j + 1)
        print(" ".join(map(str, q)))
        q = [0]
        for j in range(min(16, N)):
            if (i[1] >> j) & 1:
                q[0] += 1
                q.append(j + 1)
        print(" ".join(map(str, q)))
        break
else:
    print("No")
