def prime(max):
    Q = list(range(2, max + 1))
    A = list(range(2, max + 1))
    p = list()
    while A[0] ** 2 < max:
        B = list()
        tmp = A[0]
        p.append(tmp)
        for i in A:
            if i % tmp != 0:
                B.append(i)
            else:
                Q[i - 2] = tmp
        A = B
    p += A
    return set(p)


p = prime(10 ** 5)
p_count = [0] * (10 ** 5 + 1)
count = 0
for i in range(10 ** 5 + 1):
    if i in p and ((i + 1) // 2) in p:
        count += 1
    p_count[i] = count

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split(" "))
    print(p_count[r] - p_count[l - 1])
